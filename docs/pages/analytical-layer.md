# Analytical Layer

AIHUB Analytical layer is graph memory network used to support multi-label features and business insights for Databrick's deployed apps, analysts and non-tech stakeholders.

## Overview

```mermaid
flowchart TD
    UC["Databricks Unity Catalog"]
    UC --> A1

    subgraph AL["Analytical Layer"]
        direction TB
        A1["Customer Segments\n(Nodes)"]
        A2["Vector Encoding\n(SOM / Embeddings)"]
        A3["Cluster Comparison"]
        A1 --> A2 --> A3
    end

    A3 --> OUT["Persisted Segment Schema\nLatent Space Representations"]
    OUT --> UC
```
