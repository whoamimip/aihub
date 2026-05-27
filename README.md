# AIHUB — Your Organisation's Brand Agent

<p align="center">
  <a href="https://whoamimip.github.io">
    <img src="docs/demo_preview.gif" width="700">
  </a>
</p>

A Databricks-native intelligent application that automates the data lifecycle of your AI apps & Genie spaces by persisting chat histories and frequent questions in a unified graph memory network.

**Hackathon:** [Databricks Building Intelligent Apps with Data + AI — APJ 2026](https://buildintelligentapps-databricks.com)

# Problem Statement

Organisations with AI based solutions on Databricks face a common bottleneck in building these new gadgets.

Genie Spaces, while powerful in isolation, operate without a shared memory layer — each requiring analysts to manually re-establish context, route queries, and reconstruct institutional knowledge from scratch every session. Overtime, this utlimately leads to the key challenges:

- **Fragmented memory across AgentBricks & Genie Spaces**: no shared memory of past decisions, contextual knowledge or retaining organisation's business' metrics.
- **Absent Human Feedback Loop & Reinforcement Learning**: repetitive daily tasks in evaluating multiple Genie spaces could be time consuming which may introduce the bottlenecks AI was deployed to eliminate.

# Solution Overview

AIHub sovles these problems by building a unified memory layer which conversly also serves as an analytical layer for AI agents, analysts and non-tech business users to use in their decision making processes.

In summary, it does three things no individual Genie Space can do alone:

1. **Routes** natural language queries autonomously to the appropriate Genie Space agent without human intervention
2. **Coordinates** multi-domain questions by synthesising responses across agents into a single, coherent answer
3. **Remembers** organisation business definitions, approved metrics, business rules, and analytical decisions are stored and interconnected in a graph memory network via Unity Catalog Delta Lake, so every chat session is isolated with no clear lineage or trace.

With Databricks data stack: Unity Catalog, Genie Spaces, Apps and AgentBricks nearly, AIHUB builds a common memory network that is not only tailored to chatbots' conversations but also to the business' insights and features where both analysts and non-technical stakeholders can leverage.

## Key Features

- **User Interface**: Streamlit User interface app ready to download in your Databricks workspace and deploy via Databricks App.
- **Persisted Memory across business domains**: with Databricks Delta Lakes and Unity Catalog. Streamlit App Databricks App deployed ready features the following graph network views:
  - **The Analytical Layer**
    - Implemts ncodes customer segments as vector representations
    - Self organized clusters of your multi-label segments
  - **The Memory Graph Network unifing AI AgentBricks & GenieSpaces**
    - sorts your company’s domain knowledge through corpus embeddings and
    - automate text mining protocols to either create new benchmarks or fine-tune existing ones.
  - **AIHUB Monitor**: monitors all databricks deployed AI agents on one platform.
    - Tracks and manages the feedback loop on session agent/chat history dataset.
    - Entirely manage the lifecycle of question benchmarks for Genie spaces.

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

## Reference

- [Supervisor Agent Hierarchies](https://www.emergentmind.com/topics/supervisor-agent-hierarchies)
- [Building, Improving and Deploying Knowledge Graph RAG Systems on Databricks](https://www.databricks.com/blog/building-improving-and-deploying-knowledge-graph-rag-systems-databricks)
- [Graph Analysis Databricks Demos](https://docs.databricks.com/aws/en/machine-learning/graph-analysis)

> Built on the official Databricks [`streamlit-chatbot-app`](https://github.com/databricks/app-templates/tree/main/streamlit-chatbot-app) template, extended with supervisor agent orchestration, graph memory networking, and multi-Genie Space coordination.
> Full documentation lives in [`docs/`](docs/index.md) and is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
