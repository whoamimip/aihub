from __future__ import annotations

from datetime import datetime

import streamlit as st

DEMO_QUERY = (
    "Which customer segments are at highest churn risk this quarter, and what "
    "campaigns are currently targeting them?"
)

try:
    _GENIE_SPACE_IDS = st.secrets.get("genieSpaces", {})
except Exception:
    _GENIE_SPACE_IDS = {}

GENIE_SPACES = [
    {
        "id": "customer_analytics",
        "space_id": _GENIE_SPACE_IDS.get("customer_analytics", "customer_analytics"),
        "name": "Genie Space: Customer Analytics",
        "description": "Churn risk, retention patterns, and segment-level health.",
    },
    {
        "id": "forecast_campaign_intel",
        "space_id": _GENIE_SPACE_IDS.get("customer_needs_analysis", "forecast_campaign_intel"),
        "name": "Genie Space: Forecasting & Campaign Intelligence",
        "description": "Campaign allocation, uplift forecasts, and targeting coverage.",
    },
    {
        "id": "product_analysis",
        "space_id": _GENIE_SPACE_IDS.get("product_recommendation", "product_analysis"),
        "name": "Genie Space: Product Analysis",
        "description": "Product mix performance, basket composition, and pricing movement.",
    },
    {
        "id": "customer_subscriptions",
        "space_id": _GENIE_SPACE_IDS.get("customer_sentiment_analysis", "customer_subscriptions"),
        "name": "Genie Space: Customer Subscriptions",
        "description": "Subscription growth, plan changes, cancellations, and renewal behavior.",
    },
]

CUSTOMER_ANALYTICS_DATA = {
    "at_risk_segments": [
        {
            "segment": "Dormant Subscribers",
            "customers": 12420,
            "churn_risk": 0.41,
            "driver": "No purchase in 45+ days",
        },
        {
            "segment": "Price-sensitive Families",
            "customers": 9780,
            "churn_risk": 0.34,
            "driver": "Promo fatigue and basket shrink",
        },
        {
            "segment": "Late-night Students",
            "customers": 8360,
            "churn_risk": 0.29,
            "driver": "Competitor delivery switch",
        },
    ],
    "approved_metric_definition": {
        "metric": "Churn Rate",
        "definition": "Share of active customers with no order in the last 45 days.",
        "owner": "Customer Analytics Lead",
        "approved_on": "2026-05-20",
    },
}

CAMPAIGN_INTEL_DATA = {
    "campaigns_targeting_risk_segments": [
        {
            "campaign": "Winback Pulse Q2",
            "targets": "Dormant Subscribers",
            "budget_usd": 118000,
            "status": "Active",
            "expected_uplift": 0.16,
        },
        {
            "campaign": "Family Value Bundle",
            "targets": "Price-sensitive Families",
            "budget_usd": 92000,
            "status": "Active",
            "expected_uplift": 0.11,
        },
        {
            "campaign": "Night Owl Streak Rewards",
            "targets": "Late-night Students",
            "budget_usd": 64000,
            "status": "Active",
            "expected_uplift": 0.09,
        },
    ]
}


def now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def seed_memory_nodes() -> list[dict[str, str]]:
    return [
        {
            "id": "metric_ltv",
            "type": "Metric Definition",
            "label": "Customer Lifetime Value",
            "detail": "Net contribution over customer lifespan.",
            "source": "Finance Council",
            "updated_at": "2026-05-17 14:20:00",
        },
        {
            "id": "rule_refund_cap",
            "type": "Business Rule",
            "label": "Refund Cap Threshold",
            "detail": "Auto-approve refunds under USD 15 for loyalty tiers Gold/Silver.",
            "source": "CX Governance",
            "updated_at": "2026-05-18 09:11:00",
        },
        {
            "id": "decision_combo_reprice",
            "type": "Analytical Decision",
            "label": "Combo Repricing Policy",
            "detail": "Adjusted weekday combo price by +3% based on margin pressure.",
            "source": "Commercial Ops",
            "updated_at": "2026-05-21 16:02:00",
        },
    ]
