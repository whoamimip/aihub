# Analytical Layer

- **Purpose:** Visualizes customer segments and clusters as a graph.
- **Key logic:**
  - Loads segment/cluster data from JSON
  - Renders interactive graph with pyvis
  - Shows legend and segment index
- **File:** `pages/2_Analytical_Layer.py`

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
