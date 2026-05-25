# AIHUB — Your Organisation's Brand Agent

A Databricks-native intelligent application that orchestrates AI supervisor agents across Genie Spaces via a persistent organisational memory network — eliminating the human bottlenecks that prevent AI analytics from operating autonomously. 

**Hackathon:** [Databricks Building Intelligent Apps with Data + AI — APJ 2026](https://buildintelligentapps-databricks.com)

# Problem Statement

Organisations investing in AI analytics on Databricks face a structural coordination failure. Genie Spaces, while powerful in isolation, operate without a shared intelligence layer — each requiring analysts to manually re-establish context, route queries, and reconstruct institutional knowledge from scratch every session. This creates three compounding problems:

- Fragmented intelligence — no shared memory of past decisions, approved definitions, or analytical history exists across spaces, forcing repeated groundwork on every engagement
- Human-dependent routing — analysts act as intermediaries between business questions and the right data domain, reintroducing the bottlenecks AI was deployed to eliminate
- Zero compounding value — each interaction produces insight but leaves no lasting intelligence behind, meaning the system cannot learn or improve over time

For any business that depends on understanding its customers — their behaviour, their needs, their likelihood to disengage, and the conditions under which they return — these gaps translate directly into delayed decisions, inconsistent answers, and unrealised value from data infrastructure that has already been built.

# Solution Overview

AIHUB provides a fully managed workflow of AI Agentic orchestration layer that sits above your Genie Spaces, connecting them through shared intelligence and persistent memory. It does three things no individual Genie Space can do alone:

1. **Routes** natural language queries autonomously to the appropriate Genie Space agent without human intervention
2. **Coordinates** multi-domain questions by synthesising responses across agents into a single, coherent answer
3. **Remembers** organisation business definitions, approved metrics, business rules, and analytical decisions are stored and interconnected in a graph memory network via Lakebase, so context deepens with every session.

The result is a unified conversational interface through which analysts and non-technical stakeholders alike can interrogate complex customer data — and receive answers that are contextually accurate, organisationally consistent, and continuously improving.

## Key Features

- **Automate supervisor orchestration**: context-aware routing across multiple Genie Spaces via the Databricks Genie API and Agent Bricks API.
- **Persistent organisational memory network**: Databricks Lakebase graph memory layer that retains chat history, organisational context, and analytical decisions across sessions.
- **Analytical Memory Layer**: built-in User interface to view and manage agent memory network curated from previous chat history.

## AI Agentic Architecture

```
User / Business Stakeholder
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
