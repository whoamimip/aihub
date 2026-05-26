"""AIHUB Streamlit multipage entry point."""

import sys
import os
import logging
from pathlib import Path
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _debug_enabled() -> bool:
    env_value = os.getenv("AIHUB_DEBUG", "").strip().lower()
    if env_value in {"1", "true", "yes", "on"}:
        return True
    try:
        return bool(st.secrets.get("general", {}).get("debug", False))
    except Exception:
        return False


DEBUG_ENABLED = _debug_enabled()
APP_LOG_LEVEL = logging.DEBUG if DEBUG_ENABLED else logging.INFO
logging.basicConfig(level=APP_LOG_LEVEL)
logger = logging.getLogger("aihub")
logger.setLevel(APP_LOG_LEVEL)

st.set_page_config(
    page_title="AIHUB",
    page_icon=":material/hub:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("AIHUB")
 # Removed About AIHUB expander as requested
st.sidebar.markdown(
    """
    <a href="https://github.com/whoamimip/aihub" target="_blank" style="display:inline-flex;align-items:center;gap:0.4rem;text-decoration:none;color:inherit;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="20" height="20" fill="currentColor" aria-hidden="true">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
        </svg>
        <span>github.com/whoamimip/aihub</span>
    </a>
    """,
    unsafe_allow_html=True,
)
home_page = st.Page(
    "pages/Home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)

knowledge_base = st.Page(
    "pages/1_knowledge_base.py",
    title="Knowledge Base",
    icon=":material/account_tree:",
)

analytical_layer = st.Page(
    "pages/2_Analytical_Layer.py",
    title="Analytical Layer",
    icon=":material/scatter_plot:",
)

monitor_page = st.Page(
    "pages/3_monitor.py",
    title="Monitor",
    icon=":material/monitoring:",
)

navigation = st.navigation(
    {
        "Workspace": [home_page],
        "Operations": [knowledge_base, analytical_layer, monitor_page],
    }
)

navigation.run()

