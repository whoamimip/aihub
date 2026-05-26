""" setup_workspace.py
Utility to set up Databricks workspace client for AIHUB app.
"""

import logging
import os
from databricks.sdk import WorkspaceClient

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def setup_databricks():
    """ Set up the Databricks workspace client and return dbutils for use in the app.
    """
    if "DATABRICKS_WORKSPACE_CLIENT" not in os.environ:
        logging.info("DATABRICKS_WORKSPACE_CLIENT not found in environment variables. Initializing Databricks SDK client.")
        w = WorkspaceClient()
        dbutils = w.dbutils
    else:
        logging.info("DATABRICKS_WORKSPACE_CLIENT found in environment variables. Using existing client.")
    return dbutils
