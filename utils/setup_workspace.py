""" setup_workspace.py
Utility to set up Databricks workspace client for AIHUB app.
"""

import logging
import os
import streamlit as st
from databricks.sdk import WorkspaceClient
import json
from pathlib import Path 
    
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

@st.cache_data
def config_app():
    genie_ids = st.secrets.get("genieSpaces", {})
    return [
        {
            "id": "customer_analytics",
            "space_id": genie_ids.get("customer_analytics", "customer_analytics"),
            "name": "Genie Space: Customer Analytics",
            "description": "Churn risk, retention patterns, and segment-level health.",
        },
        {
            "id": "forecast_campaign_intel",
            "space_id": genie_ids.get("customer_needs_analysis", "forecast_campaign_intel"),
            "name": "Genie Space: Forecasting & Campaign Intelligence",
            "description": "Campaign allocation, uplift forecasts, and targeting coverage.",
        },
        {
            "id": "product_analysis",
            "space_id": genie_ids.get("product_recommendation", "product_analysis"),
            "name": "Genie Space: Product Analysis",
            "description": "Product mix performance, basket composition, and pricing movement.",
        },
        {
            "id": "customer_subscriptions",
            "space_id": genie_ids.get("customer_sentiment_analysis", "customer_subscriptions"),
            "name": "Genie Space: Customer Subscriptions",
            "description": "Subscription growth, plan changes, cancellations, and renewal behavior.",
        },
    ]

@st.cache_data
def load_mock_data():
    """ loads mock dataset for streamlit visuals testing """

    data_path = Path(__file__).parent.parent / 'data'
    assert data_path.exists(), f"Data path {data_path} does not exist. Please ensure the data directory is in place with the required mock data files."
    mocks = {}
    for f in data_path.glob("*.json"):
        with open(f, "r") as file:
            mocks[f.stem] = json.load(file)
    return mocks
