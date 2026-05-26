""" 
src/genie_manager.py

"""
import json
import requests
from ..utils.setup_workspace import setup_workspace

dbutils = setup_workspace()

class GenieSpaceEvent:
    def __init__(
        self,
        genie_space_id: str,
        databricks_host = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get(),
        token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
    ):
        self.genie_space_id = genie_space_id
        self.databricks_host = databricks_host
        self.path_url = f"{self.databricks_host}/api/2.0/genie/spaces/{self.genie_space_id}"
        self.headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        self._init()

    def _init(self):
        try:
            self.fetch_genie_space_config(space_id=self.genie_space_id)
            self.workspace = json.loads(self.config.get('serialized_space', "{}"))
            if len(self.workspace) == 0 or not set(['version', 'data_sources', 'instructions', 'benchmarks']).issubset(set(self.workspace.keys())): raise ValueError('error')
            self.current = self.workspace.get('benchmarks', {}).get('questions', [])
        except Exception as e:
            raise ValueError(f"Error fetching genie space: {str(e)}")

    def fetch_genie_space_config(self, space_id: str) -> dict:
        """Fetch the full Genie Space configuration including serialized_space. Initially provoked to grab space's data. """

        url = f"{self.databricks_host}/api/2.0/genie/spaces/{space_id}"
        params = {"include_serialized_space": "true"}
        resp = requests.get(url, headers=self.headers, params=params)
        resp.raise_for_status()
        self.config = resp.json()
        if not set(['space_id', 'title', 'description', 'warehouse_id', 'parent_path', 'serialized_space', 'etag']).issubset(set(self.config.keys())): raise ValueError('error')

    @property
    def list_all_genie_spaces(self):
        url = f"{self.databricks_host}/api/2.0/genie/spaces"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        spaces = resp.json().get("spaces", [])
        return [
            {"space_id": s.get("space_id"), "title": s.get("title")}
            for s in spaces
        ] 
        
    def update(self, questions: list):
        print(f'Current existing {len(self.current)}')
        self.current.extend(questions)
        print(f"Updated qs with {len(questions)} new qs. New len: {len(self.current)}")

    def store(self):
        self.workspace.get('benchmarks')['questions'] = self.current
        inputs = {'serialized_space': json.dumps(self.workspace)}
        response = requests.patch(self.patch_url, headers=self.headers, json=inputs)
        response.raise_for_status()

    def list(self):
        return self.current

if __name__ == "__main__":
    genie = GenieSpaceEvent('01f13ecd8f1615e4aff0458e17b496a6')
    genie.list()

