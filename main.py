""" 
mymcaihub/app.py
This is the main entry point for the My McBricks app. It sets up the navigation and loads the different pages of the app.
"""

import logging
import os
import sys
from pathlib import Path

import streamlit as st

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SERVING_ENDPOINT = os.getenv('SERVING_ENDPOINT')
assert SERVING_ENDPOINT, \
    ("Unable to determine serving endpoint to use for chatbot app. If developing locally, "
     "set the SERVING_ENDPOINT environment variable to the name of your serving endpoint. If "
     "deploying to a Databricks app, include a serving endpoint resource named "
     "'serving_endpoint' with CAN_QUERY permissions, as described in "
     "https://docs.databricks.com/aws/en/generative-ai/agent-framework/chat-app#deploy-the-databricks-app")

# Check if the endpoint is supported
endpoint_supported = is_endpoint_supported(SERVING_ENDPOINT)

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

st.set_page_config(
    page_title="AIHub",
    page_icon=":material/auto_awesome:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("AIHub")
st.sidebar.header("Navigation")
st.sidebar.markdown("Use the navigation below to explore different sections of the app.")

# --- Home Page ---
home_page = st.Page(
    "pages/Home.py",
    title="Home",
    icon=":material/home:",
    default=True
)
# --- AI Section ---
knowledge_base = st.Page(
    "pages/1_knowledge_base.py",
    title="Knowledge Base",
    icon=":material/menu_book:"
)

ai_pages = [knowledge_base]
pages = {
    "Content": [home_page],
    "AI": ai_pages
}
pg = st.navigation(pages)

pg.run()

