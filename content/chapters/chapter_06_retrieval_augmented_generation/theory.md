# Chapter 06: Retrieval-Augmented Generation in Oncology

## Learning Objectives

By the end of this chapter, you will:

- explain why retrieval-augmented generation (RAG) is essential for biomedical reliability
- design oncology document pipelines for chunking, metadata tagging, and indexing
- compare sparse and dense retrieval strategies for scientific evidence search
- build grounded answer workflows that preserve citations and uncertainty signals
- evaluate RAG systems for retrieval quality, factuality, and clinical safety constraints

---

## Introduction

Biomedical knowledge changes continuously. New clinical trials, variant interpretations, and translational studies can shift what is considered actionable. A model relying only on parametric memory cannot reliably keep pace with this update cycle. Retrieval-augmented generation (RAG) addresses this problem by retrieving relevant external evidence at inference time and conditioning generation on those sources.

In oncology, RAG is not only a performance optimization. It is a traceability mechanism. By grounding responses in identifiable documents, RAG makes outputs auditable and easier to challenge when evidence is incomplete, conflicting, or outdated.

This chapter covers practical RAG design choices for cancer research: what to index, how to retrieve, how to synthesize, and how to evaluate reliability before integrating into agent workflows.

---

## 6.1 Why RAG Matters for Biomedical Systems

Without retrieval, LLMs may generate plausible responses that cannot be tied to current evidence. RAG reduces this risk by introducing a retrieval step before synthesis.

### Key Benefits in Oncology

- grounding answers in source text
- improving updateability without full model retraining
- exposing provenance for review and audit
- enabling domain-specific scope control

### Typical Biomedical Failure Without RAG

- outdated treatment context presented as current
- unsupported linkage between mutation and therapy
- missing caveats for cohort context or pediatric applicability
- fabricated citation statements

RAG does not eliminate errors, but it changes them into inspectable errors.

---

## 6.2 Core RAG Pipeline Components

A practical oncology RAG system usually includes five layers.

```text
Corpus Ingestion -> Chunking + Metadata -> Embedding/Indexing -> Retrieval -> Grounded Synthesis
```

### 1. Corpus Ingestion

Potential sources include:

- PubMed abstracts and full-text subsets
- guideline summaries and curated evidence databases
- internal cohort reports and pathology notes
- variant annotation exports from validated tools

### 2. Chunking and Metadata

Each document is split into chunks and tagged with metadata such as:

- source and publication date
- cancer subtype and disease ontology terms
- modality (clinical, genomic, functional, trial)
- evidence level or curation status

### 3. Indexing

- dense vector index for semantic similarity
- optional sparse/BM25 index for precise keyword matches
- hybrid ranking layer to balance recall and precision

### 4. Retrieval

Top candidate chunks are selected using query embedding and filters.

### 5. Grounded Synthesis

LLM generates an answer constrained to retrieved evidence and citation references.

---

## 6.3 Chunking Strategy for Biomedical Text

Chunking is one of the highest-impact design decisions in RAG.

### Common Chunking Options

- fixed-length chunks by token count
- sentence-boundary chunks with overlap
- section-aware chunks (methods, results, conclusion)
- entity-aware chunks centered on genes, variants, or diseases

### Trade-Offs

- very small chunks: high precision but fragmented context
- very large chunks: better context but noisier retrieval

### Practical Oncology Guidance

- keep chunks large enough to include claim plus qualifier
- preserve adjacency for statements about population and effect size
- store document section metadata to support reranking

In biomedical writing, qualifiers are often far from the main claim. Chunking should preserve that relationship.

---

## 6.4 Retrieval Methods: Sparse, Dense, and Hybrid

No single retriever dominates across all oncology queries.

### Sparse Retrieval (for example, BM25)

- strength: exact term matching, useful for gene symbols and variant strings
- weakness: misses semantically related phrasing

### Dense Retrieval (embedding-based)

- strength: semantic matching across paraphrases
- weakness: can retrieve conceptually similar but context-misaligned text

### Hybrid Retrieval

Combines sparse and dense scores, often with reranking.

- strength: better robustness for mixed query types
- weakness: additional tuning complexity

For biomedical tasks with both strict entities and fuzzy concepts, hybrid retrieval is often the most reliable baseline.

---

## 6.5 Query Construction and Reformulation

User queries are often underspecified. Effective RAG systems rewrite or expand queries before retrieval.

### Query Augmentation Inputs

- normalized gene and alias terms
- disease ontology mappings
- assay modality constraints
- temporal constraints (for example, last 5 years)

### Example

User query:
"Is EGFR L858R actionable?"

Possible retrieval query expansion:

- entity: EGFR, L858R
- context: non-small cell lung cancer, lung adenocarcinoma
- evidence type: clinical interpretation, actionability
- filter: curated knowledge base + recent reviews

Query reformulation improves recall while preserving context relevance.

---

## 6.6 Grounded Generation and Citation Design

Generation should be conditioned on retrieved passages and constrained by explicit evidence rules.

### Recommended Answer Structure

1. claim summary
2. evidence snippets with source IDs
3. uncertainty and conflict notes
4. suggested next retrieval or review step

### Citation Requirements

- every high-impact claim maps to one or more retrieved source IDs
- unsupported claims are explicitly marked as unresolved
- citations should include source metadata (title, year, database, ID)

Grounded output is not only safer. It also reduces reviewer workload.

---

## 6.7 Evaluation Framework for Oncology RAG

RAG quality must be measured across retrieval and generation stages.

### Retrieval Metrics

- recall at k
- precision at k
- mean reciprocal rank (MRR)
- coverage of required evidence categories

### Generation Metrics

- grounded claim rate
- citation fidelity
- unsupported claim rate
- clinical safety review outcomes

### End-to-End Operational Metrics

- time-to-useful-answer for analysts
- human edit distance
- escalation rate for unresolved evidence

Benchmark sets should include edge cases such as pediatric contexts, rare variants, and conflicting studies.

---

## 6.8 Common Failure Modes and Mitigations

### Failure Mode 1: Retrieval Misses Critical Evidence

- cause: weak query mapping or poor metadata filters
- mitigation: hybrid retrieval and ontology-aware expansion

### Failure Mode 2: Irrelevant but Fluent Synthesis

- cause: model over-prioritizes language priors over retrieved text
- mitigation: evidence-only prompts and citation-required output schemas

### Failure Mode 3: Conflicting Sources Collapsed Into False Consensus

- cause: naive summarization prompts
- mitigation: conflict-detection step before final synthesis

### Failure Mode 4: Stale Index

- cause: infrequent corpus updates
- mitigation: scheduled re-indexing and source freshness checks

In biomedical workflows, stale retrieval is a silent but high-impact risk.

---

## 6.9 Integration With Agents and Tooling

RAG often serves as the factual substrate for multi-step agents.

```text
Planner Agent -> Query Builder -> Retriever -> Evidence Validator -> LLM Synthesizer -> Reviewer Interface
```

### Integration Guidelines

- keep retrieval outputs structured for downstream tool compatibility
- include provenance fields in memory/state objects
- separate retrieval tools by evidence type where feasible
- preserve unresolved questions for follow-up agent steps

This architecture makes agent behavior easier to inspect and debug.

---

## 6.10 Governance, Security, and Access Control

Biomedical RAG systems may combine public and controlled sources. Governance must be explicit.

### Governance Controls

- access-aware retrieval filters for controlled datasets
- audit logs for retrieval queries and returned snippets
- data-use policy tags propagated into generation prompts
- retention policies for cached retrieval artifacts

### Safety Controls

- automatic warning when evidence coverage is sparse
- mandatory human review flags for high-impact outputs
- policy checks before exposing trial or treatment-oriented content

Reliable RAG in oncology requires data governance and model governance together.

---

## Key Takeaways

- RAG is foundational for biomedical reliability because it grounds generation in explicit evidence.
- Chunking and metadata design strongly affect retrieval quality and downstream factuality.
- Hybrid retrieval is often a strong default for oncology queries mixing strict entities and semantic intent.
- Grounded synthesis should require citations, uncertainty labels, and conflict handling.
- RAG evaluation must measure retrieval, generation, and operational usefulness together.
- Agentic oncology systems work best when retrieval outputs are structured, auditable, and governance-aware.

---

## References

1. Lewis P, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS. 2020.
2. Karpukhin V, et al. Dense Passage Retrieval for Open-Domain Question Answering. EMNLP. 2020.
3. Robertson S, Zaragoza H. The Probabilistic Relevance Framework: BM25 and Beyond. 2009.
4. Gao Y, et al. Retrieval-Augmented Generation for Large Language Models: A Survey. 2023.
5. Singhal K, et al. Large Language Models Encode Clinical Knowledge. Nature. 2023.

---

## Further Reading

- Biomedical information retrieval benchmarks and shared tasks
- Engineering guides for vector databases and hybrid search
- Clinical AI governance frameworks for evidence-linked decision support

