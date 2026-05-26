# AIHUB — Your Organisation's Brand Agent

A Databricks-native intelligent application that orchestrates AI supervisor agents across Genie Spaces via a persistent organisational memory network — eliminating the human bottlenecks that prevent AI analytics from operating autonomously.

**Hackathon:** [Databricks Building Intelligent Apps with Data + AI — APJ 2026](https://buildintelligentapps-databricks.com)

# Problem Statement

Organisations with AI based solutions on Databricks face a common bottleneck in building, managing the validating these new gadgets.

Genie Spaces, while powerful in isolation, operate without a shared memory layer — each requiring analysts to manually re-establish context, route queries, and reconstruct institutional knowledge from scratch every session. Overtime, this utlimately leads to the key challenges:

- Fragmented memory across AgentBricks & Genie Spaces: no shared memory of past decisions, contextual knowledge or retaining organisation's business' metrics.
- Reinforcement Learning: each interaction produces insight but leaves no lasting intelligence behind, meaning the system cannot learn or improve over time. This leads to analysts becoming the intermediaries between business questions and the right data domain - reintroducing the bottlenecks AI was deployed to eliminate.

For any business that depends on understanding its customers for e.g. their behaviour, their needs, their likelihood to disengage, and the conditions under which they return — these gaps translate directly into delayed decisions, inconsistent answers, and unrealised value from data infrastructure that has already been built.

# Solution Overview

AIHUB provides a fully managed workflow of AI Agentic orchestration layer that sits above your AI solutions & Genie Spaces, connecting them through one common graph memory network - built to persist your organisation's contextual information and organised chat history organisations.

In summary, it does three things no individual Genie Space can do alone:

1. **Routes** natural language queries autonomously to the appropriate Genie Space agent without human intervention
2. **Coordinates** multi-domain questions by synthesising responses across agents into a single, coherent answer
3. **Remembers** organisation business definitions, approved metrics, business rules, and analytical decisions are stored and interconnected in a graph memory network via Lakebase, so context deepens with every session.

With Databricks data stack: Unity Catalog, Genie Spaces, Apps and AgentBricks nearly, AIHUB builds a unified memory network not only tailored to chatbots' conversations but also to the business' insights and features where both analysts and non-technical stakeholders can leverage. Beneath this is the AI Agentic evaluation workflows that could accelerate analysts' bottlenecks in evaluating and monitoring AI spaces on Databricks.

## Key Features

- **Analytical Memory Layer**: Streamlit User interface app ready to download in your Databricks workspace and deploy via Databricks App.
- **Persisted Memory across business domains**: with Databricks Delta Lakes and Unity Catalog. Streamlit App Databricks App deployed ready features the following graph network views:
  - The Analytical Knowledge Base
    - Implemts ncodes customer segments as vector representations
    - Self organized clusters of your multi-label segments
  - The Memory Graph Network unifing AI AgentBricks & GenieSpaces
    - sorts your company’s domain knowledge through corpus embeddings and
    - automate text mining protocols to either create new benchmarks or fine-tune existing ones.
  - The Monitoring Layer closes the feedback loop:
    - automate data preprocessing workflows on AI Agent chat histories
    - automate evaluation benchmarks for AgentBricks & Genie spaces

## AI Agentic Architecture

```
User Interface
           │
           ▼
┌──────────────────────────┐
│    Databricks App (UI)   │  ← Unified natural language interface
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   Supervisor Agent       │  ← Agent Bricks: orchestrates routing, coordinates multi-domain responses
└─────┬──────────┬─────────┘
      │          │
      ▼          ▼
┌──────────┐  ┌─────────────────────┐
│  Genie   │  │  Genie Space:       │
│  Space:  │  │  Forecasting &      │
│ Customer │  │  Campaign Intel     │
│ Analytics│  └──────────┬──────────┘
└─────┬────┘             │
      └──────────┬────────┘
                 ▼
┌──────────────────────────┐
│  Lakebase                │  ← Persistent memory: brand context,
│  (Organisational Memory) │    domain glossary, session history,
└──────────────────────────┘    analytical decisions & approved metrics
```

## Project Directory Summary

```bash
.
├── main.py                    # Streamlit App bootstrap entry point
├── requirements.txt           # App's dependencies
├── utils/                     # Streamlit & Databricks SDK config / utils helpers
├── app/                       # AIHub Core application package
│   ├── notebooks/             # Jupyter Notebook Demos
│   ├── src/                   # AIHub Source Scripts
│   └── tests/                 # Tests
└── pages/                     # Streamlit multipage
      ├── 1_knowledge_base.py    # Knowledge Graph Network Viewer
      ├── 2_monitor.py           # Genie Space Monitoring page
      └── Home.py                # Home/landing page & UI Chatbot with your Brand Agent
```

## Documentation

Full documentation lives in [`docs/`](docs/index.md) and is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

```bash
pip install -r requirements-docs.txt
mkdocs serve   # http://localhost:8000
```

Sections: end-to-end [architecture](docs/architecture/overview.md), [local development](docs/setup/local-dev.md), [Databricks App deployment](docs/deployment/databricks.md), and [per-page user guides](docs/pages/index.md).

## Reference

- [Supervisor Agent Hierarchies](https://www.emergentmind.com/topics/supervisor-agent-hierarchies)
- [Building, Improving and Deploying Knowledge Graph RAG Systems on Databricks](https://www.databricks.com/blog/building-improving-and-deploying-knowledge-graph-rag-systems-databricks)
- [Graph Analysis Databricks Demos](https://docs.databricks.com/aws/en/machine-learning/graph-analysis)

> Built on the official Databricks [`streamlit-chatbot-app`](https://github.com/databricks/app-templates/tree/main/streamlit-chatbot-app) template, extended with supervisor agent orchestration, graph memory networking, and multi-Genie Space coordination.
