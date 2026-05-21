# Chapter 11: Knowledge Graphs and Biomedical Reasoning

## Learning Objectives

By the end of this chapter, you will:

- explain how biomedical knowledge graphs support reasoning beyond document retrieval
- design graph schemas for genes, variants, diseases, therapies, evidence, and cohorts
- apply ontology alignment and entity normalization for cross-source integration
- build graph-aware retrieval and reasoning workflows for oncology agents
- evaluate graph quality, reasoning validity, and governance constraints in production settings

---

## Introduction

Biomedical evidence is highly relational. A mutation can affect a gene, which links to pathways, therapies, resistance mechanisms, and disease subtypes. Text documents contain these facts, but the connections are often implicit, fragmented, and difficult to query systematically. Knowledge graphs (KGs) represent this structure explicitly through entities and relationships, enabling more transparent reasoning workflows.

In cancer research, KGs can connect variant interpretation databases, cohort statistics, pathway resources, and literature-derived evidence into a unified substrate for agentic AI. This does not replace retrieval systems. Instead, it complements them by making relational constraints and provenance visible at query time.

This chapter covers knowledge-graph design for oncology reasoning, with emphasis on schema quality, provenance, graph-aware retrieval, and safe integration with LLM-based agents.

---

## 11.1 Why Knowledge Graphs for Biomedical AI

LLMs and vector search are useful for semantic retrieval, but they are weak at explicit relational guarantees. KGs provide structure where relation type matters.

### Where KGs Add Value

- explicit representation of entity-relation semantics
- path-based reasoning across multi-hop biomedical evidence
- constraint-aware queries (for example tumor type, evidence level, temporal scope)
- improved explainability through visible relationship chains

### Typical Oncology Questions Suited to Graph Reasoning

- which therapies are linked to a variant in a specific disease context?
- what evidence paths connect a pathway perturbation to resistance?
- which biomarkers have conflicting interpretations across sources?

Graphs make these questions easier to answer reproducibly.

---

## 11.2 Core Graph Modeling Concepts

A biomedical KG usually represents facts as triples:

$$
(subject,\ relation,\ object)
$$

Examples:

- `(EGFR_L858R, associated_with, Lung_Adenocarcinoma)`
- `(CIViC_EID_1234, supports, EGFR_TKI_Sensitivity_Claim)`
- `(Claim_X, has_evidence_level, Tier_A)`

### Graph Building Blocks

- nodes (entities): genes, variants, diseases, drugs, studies, claims
- edges (relations): associated_with, inhibits, confers_resistance_to, supported_by
- properties: source, timestamp, confidence, license, ontology IDs

### Modeling Principle

Prefer explicit typed relations over generic links. Semantic precision improves query reliability.

---

## 11.3 Ontologies and Entity Normalization

Graph quality depends on consistent identifiers and ontology mapping.

### Common Biomedical Mapping Targets

- genes: HGNC, Ensembl
- diseases: Disease Ontology, OncoTree, ICD crosswalks
- variants: HGVS, reference-build-aware coordinates
- drugs: standardized compound identifiers

### Frequent Normalization Challenges

- synonym ambiguity (for example legacy gene symbols)
- disease term granularity mismatch
- variant representation differences across sources
- implicit context missing in free-text assertions

Entity normalization should be versioned and auditable, not silently applied.

---

## 11.4 Building Oncology Knowledge Graphs

A practical graph pipeline includes extraction, normalization, validation, and publication stages.

### Recommended Pipeline

1. ingest structured and unstructured biomedical sources
2. extract candidate entities and relations
3. normalize identifiers and map ontologies
4. attach provenance and evidence metadata
5. validate schema and semantic constraints
6. publish graph snapshots for query and retrieval

### Minimum Provenance Fields per Edge

- source database or document ID
- extraction method and version
- timestamp and graph release version
- confidence score and evidence type

Without edge-level provenance, graph reasoning becomes difficult to trust.

---

## 11.5 Querying and Reasoning Over Graphs

Graph queries can capture relational constraints that are cumbersome in plain text retrieval.

### Query Modes

- neighborhood queries: immediate context around a node
- path queries: multi-hop relation chains
- constrained subgraph queries: filter by evidence level, date, or disease context
- aggregation queries: count support/conflict across evidence sources

### Reasoning Patterns

- mechanistic path tracing
- evidence triangulation across databases
- contradiction detection between claims
- candidate prioritization under explicit constraints

Graph results should be returned with both path explanations and source citations.

---

## 11.6 Graph + LLM Hybrid Architectures

Knowledge graphs and LLMs are complementary.

```text
User Query -> Graph Retrieval/Traversal -> Evidence Subgraph -> LLM Synthesis -> Structured, Cited Output
```

### Benefits of Hybrid Design

- graph enforces relational constraints
- LLM improves natural-language synthesis and usability
- cited subgraphs make outputs auditable

### Guardrails

- LLM must not invent relations absent from graph context
- unresolved graph conflicts must be surfaced, not resolved implicitly
- synthesis prompts should include evidence-count and confidence fields

Hybrid systems work best when graph output is treated as a strict reasoning substrate.

---

## 11.7 Knowledge Graphs in Agentic Workflows

Agents can use KGs as memory and reasoning infrastructure.

### Agent Roles With Graph Access

- retrieval agent: fetches relevant subgraphs by query constraints
- reasoner agent: evaluates paths and conflict patterns
- critic agent: checks unsupported inference jumps
- report agent: converts graph evidence to analyst-facing narratives

### Operational Advantages

- faster evidence linking across heterogeneous sources
- transparent explanation paths for review
- easier incremental updates than full model retraining

Agent behavior is more predictable when graph interfaces are explicit and typed.

---

## 11.8 Evaluation of Biomedical Knowledge Graph Systems

Evaluation must measure structural, semantic, and task-level quality.

### Structural Metrics

- node/edge coverage across target domains
- ontology mapping completeness
- schema conformance rate

### Semantic Metrics

- relation precision/recall against curated references
- contradiction rate and conflict resolution quality
- provenance completeness

### Task Metrics

- improvement in retrieval-grounded QA correctness
- analyst time saved in evidence tracing
- reduction in unsupported claims in generated reports

No single metric captures graph utility. Use a layered evaluation strategy.

---

## 11.9 Governance, Licensing, and Data Rights

Biomedical graph construction often combines sources with different licenses and access rules.

### Governance Requirements

- preserve source-specific licensing metadata
- enforce access controls for restricted data edges
- maintain audit logs for graph updates and query access
- version graph releases with reproducible build manifests

### Safety Considerations

- prohibit uncited high-impact claims in user-facing outputs
- flag low-support relation paths before synthesis
- require human review for clinically sensitive reasoning outputs

Governance controls should be embedded in graph build and query layers, not bolted on afterward.

---

## 11.10 Practical Blueprint for Oncology KG Deployment

1. define ontology-aligned schema for core oncology entities and relations
2. ingest high-value curated sources first (variants, therapies, disease hierarchies)
3. add literature-derived relations with confidence and provenance tags
4. expose query APIs with constrained relation types and filters
5. integrate with LLM/agent layers for cited synthesis and review workflows

A staged rollout limits risk while delivering immediate utility.

---

## Key Takeaways

- Knowledge graphs provide explicit relational structure that complements LLM and vector retrieval systems.
- Oncology graph quality depends on entity normalization, typed relations, and edge-level provenance.
- Graph-aware reasoning improves explainability and constraint handling in agent workflows.
- Hybrid graph + LLM pipelines can improve usability without sacrificing traceability.
- Evaluation should combine structural, semantic, and task-level metrics.
- Licensing, access control, and governance are first-class graph design requirements.

---

## References

1. Hogan A, et al. Knowledge Graphs. ACM Computing Surveys. 2021.
2. Himmelstein DS, et al. Systematic Integration of Biomedical Knowledge Prioritizes Drugs for Repurposing. eLife. 2017.
3. Rotmensch M, et al. Learning a Health Knowledge Graph from Electronic Medical Records. Scientific Reports. 2017.
4. Gao Y, et al. Retrieval-Augmented Generation for Large Language Models: A Survey. 2023.
5. Haendel MA, et al. A Census of Disease Ontologies. Annual Review of Biomedical Data Science. 2020.

---

## Further Reading

- Graph database documentation and graph query language guides
- Biomedical ontology integration best practices
- Knowledge-graph explainability patterns for clinical and translational AI

