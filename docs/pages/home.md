# AI Agentic Architecture

Brief on Brand Agent (Supervisor) and Genie Spaces.

## Supervisor Agent

A Supervisor Agent, built on Agent Bricks, performs two functions:

- **Chat History Summarisation & transformations** — incoming session/chat histories, traces on agent's thought process or SQL natural language queries are classified by context inferred from its vector space representation ( `sentence-transformers` ).
- **Query routing** — queries are routed to the appropriate Genie Space, organised by organisational context. For this proof of concept, the domain is customer churn and retention. Representative Genie Spaces include Customer Analytics, Subscription Models, and Customer Cohort Forecasting.

```mermaid
flowchart LR
    Q["Incoming Query"]
    IC["Intent Classifier\nAgent Bricks"]
    R{"Domain\nRouter"}
    GS1["Genie Space\nCustomer Analytics"]
    GS2["Genie Space\nSubscription Models"]
    GS3["Genie Space\nCohort Forecasting"]
    SYN["Response Synthesiser"]
    OUT["Unified Output"]

    Q --> IC
    IC --> R
    R -->|Customer behaviour| GS1
    R -->|Subscription & revenue| GS2
    R -->|Forecast & cohort| GS3
    GS1 & GS2 & GS3 --> SYN
    SYN --> OUT
```

## Memory Layer

AIHUB addresses the absence of persistent state by constructing a unified memory layer, which concurrently serves as an analytical layer accessible to AI agents, analysts, and non-technical business users.

The memory layer is a structured data topology that organises information as an interconnected network. Rather than storing data in flat tables, it maps entities as **nodes** and relationships as **edges**.

Examples include:

- Nodes representing organisational domain members, with edges weighted by chat domain frequency.
- Nodes representing customer multi-label segments, connected to insights drawn from Agent Bricks and Genie Space interactions.

```mermaid
flowchart TD
    UC["Databricks Unity Catalog\nDelta Tables"]

    UC --> AL
    UC --> KB
    UC --> ML

    subgraph AL["Analytical Layer"]
        A1["Customer Segment Nodes"]
        A2["Vector Encoding — SOM"]
        A3["L2 Distance Cluster Comparison"]
        A4["Persisted Segment Schema\nNo Manual Redefinition"]
        A1 --> A2 --> A3 --> A4
    end

    subgraph KB["Knowledge Base Graph"]
        K1["Organisational Domain Nodes"]
        K2["Corpus Embeddings\nCosine Similarity Edges"]
        K3["Curated Genie Space\nChat Histories"]
        K4["Ranked Domain Retrieval"]
        K1 --> K2 --> K3 --> K4
    end

    subgraph ML["Monitoring Layer"]
        M1["Fetch Last K=5\nAgent Interactions"]
        M2["Summarise — Agent Bricks\n2–3 sentences"]
        M3["Encode + Store\nUnity Catalog"]
        M4["Measure vs Clusters\nPCA + KMeans"]
        M1 --> M2 --> M3 --> M4
    end

    A4 & K4 & M4 --> FB["Compounding Memory Topology\nPersistent · Ranked · Self-updating"]
    FB -->|Retrieved context| SUP["Supervisor Agent"]
```
