# Local development

Run AIHUB on your laptop against mock data, then optionally connect to live Databricks Genie Spaces.

## Prerequisites

- Python 3.10+ (matches the Databricks Apps runtime).
- `git`.
- (Optional) A Databricks workspace with Genie enabled and a Model Serving endpoint, if you want to run against live spaces.

## Install

```bash
git clone https://github.com/whoamimip/aihub.git
cd aihub

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Configure secrets

Create `.streamlit/secrets.toml` (this file is not committed). Use placeholders to start — AIHUB falls back to seeded mock data when live credentials aren't available.

```toml
[general]
debug = true

[databricks]
host  = "https://<your-workspace>.cloud.databricks.com"
token = "dapi-************"

[genie]
customer_analytics      = "01ef0000-0000-0000-0000-000000000000"
forecasting_campaign    = "01ef0000-0000-0000-0000-000000000001"
product_analysis        = "01ef0000-0000-0000-0000-000000000002"
customer_subscriptions  = "01ef0000-0000-0000-0000-000000000003"

[openai]
api_key = "sk-************"
```

## Run

```bash
streamlit run main.py
```

Open [http://localhost:8501](http://localhost:8501).
