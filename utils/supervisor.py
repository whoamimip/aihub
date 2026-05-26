from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import streamlit as st

from utils.mock_data import (
    CAMPAIGN_INTEL_DATA,
    CUSTOMER_ANALYTICS_DATA,
    DEMO_QUERY,
    GENIE_SPACES,
    now_iso,
    seed_memory_nodes,
)


@dataclass
class SupervisorResult:
    query: str
    routed_space_ids: list[str]
    intent_labels: list[str]
    domain_findings: list[str]
    final_answer: str
    latency_ms: int


def init_demo_state() -> None:
    if "aihub_chat" not in st.session_state:
        st.session_state.aihub_chat = [
            {
                "role": "assistant",
                "content": (
                    "Brand Agent online. Ask a cross-domain business question and I will "
                    "classify intent, route to Genie Spaces, and synthesize one answer."
                ),
            }
        ]

    if "aihub_active_spaces" not in st.session_state:
        st.session_state.aihub_active_spaces = []

    if "aihub_memory_nodes" not in st.session_state:
        st.session_state.aihub_memory_nodes = seed_memory_nodes()

    if "aihub_events" not in st.session_state:
        st.session_state.aihub_events = []

    if "aihub_kpis" not in st.session_state:
        st.session_state.aihub_kpis = {
            "total_queries": 0,
            "cross_domain_queries": 0,
            "manual_routing_events": 0,
            "avg_latency_ms": 0.0,
        }


def classify_intent(query: str) -> list[str]:
    lowered = query.lower()
    labels = []
    if "churn" in lowered or "segment" in lowered or "customer" in lowered:
        labels.append("customer_risk")
    if "campaign" in lowered or "target" in lowered or "uplift" in lowered:
        labels.append("campaign_effectiveness")
    if not labels:
        labels.append("general_analytics")
    return labels


def route_query(intent_labels: list[str]) -> list[str]:
    routed = []
    if "customer_risk" in intent_labels or "general_analytics" in intent_labels:
        routed.append("customer_analytics")
    if "campaign_effectiveness" in intent_labels or "general_analytics" in intent_labels:
        routed.append("forecast_campaign_intel")
    return routed


def _build_findings() -> list[str]:
    top_risk = CUSTOMER_ANALYTICS_DATA["at_risk_segments"][0]
    top_campaign = CAMPAIGN_INTEL_DATA["campaigns_targeting_risk_segments"][0]
    return [
        (
            f"Highest churn-risk segment is {top_risk['segment']} at "
            f"{top_risk['churn_risk'] * 100:.1f}% risk ({top_risk['customers']:,} customers)."
        ),
        (
            f"Active campaign targeting that segment is {top_campaign['campaign']} "
            f"with expected uplift of {top_campaign['expected_uplift'] * 100:.1f}%."
        ),
    ]


def _build_final_answer(findings: list[str]) -> str:
    return (
        "Supervisor synthesis across Customer Analytics and Forecasting/Campaign Intelligence:\n"
        f"- {findings[0]}\n"
        f"- {findings[1]}\n"
        "No manual routing was required. Context was resolved from prior organizational memory where available."
    )


def _upsert_churn_definition_node() -> None:
    churn_metric = CUSTOMER_ANALYTICS_DATA["approved_metric_definition"]
    nodes = st.session_state.aihub_memory_nodes
    node_id = "metric_churn_rate"

    for node in nodes:
        if node["id"] == node_id:
            node["detail"] = churn_metric["definition"]
            node["updated_at"] = now_iso()
            return

    nodes.append(
        {
            "id": node_id,
            "type": "Metric Definition",
            "label": churn_metric["metric"],
            "detail": churn_metric["definition"],
            "source": churn_metric["owner"],
            "updated_at": now_iso(),
        }
    )


def _record_monitor_event(result: SupervisorResult) -> None:
    st.session_state.aihub_events.append(
        {
            "timestamp": now_iso(),
            "query": result.query,
            "spaces": ", ".join(result.routed_space_ids),
            "status": "success",
            "latency_ms": result.latency_ms,
            "intent": ", ".join(result.intent_labels),
        }
    )


def _update_kpis(result: SupervisorResult) -> None:
    kpis = st.session_state.aihub_kpis
    kpis["total_queries"] += 1
    if len(result.routed_space_ids) > 1:
        kpis["cross_domain_queries"] += 1

    current_total = kpis["total_queries"]
    previous_average = kpis["avg_latency_ms"]
    kpis["avg_latency_ms"] = ((previous_average * (current_total - 1)) + result.latency_ms) / current_total


def run_supervisor(query: str) -> SupervisorResult:
    intent_labels = classify_intent(query)
    routed_space_ids = route_query(intent_labels)
    findings = _build_findings()
    final_answer = _build_final_answer(findings)

    result = SupervisorResult(
        query=query,
        routed_space_ids=routed_space_ids,
        intent_labels=intent_labels,
        domain_findings=findings,
        final_answer=final_answer,
        latency_ms=860,
    )

    st.session_state.aihub_active_spaces = routed_space_ids
    _upsert_churn_definition_node()
    _record_monitor_event(result)
    _update_kpis(result)

    return result


def append_chat(role: str, content: str) -> None:
    st.session_state.aihub_chat.append({"role": role, "content": content})


def render_chat_history() -> None:
    for message in st.session_state.aihub_chat:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def genie_space_lookup() -> dict[str, dict[str, Any]]:
    return {space["id"]: space for space in GENIE_SPACES}


def scripted_query() -> str:
    return DEMO_QUERY
