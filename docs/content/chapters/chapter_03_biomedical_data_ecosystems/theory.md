# Chapter 03: Biomedical Data Ecosystems

## Learning Objectives

By the end of this chapter, you will:

- identify the major public oncology and biomedical repositories used in AI workflows
- identify major pediatric oncology databases and portals and their integration constraints
- distinguish clinical, molecular, functional, and literature-derived data products
- design reproducible data acquisition and harmonization pipelines for multi-source studies
- evaluate data quality, bias, and licensing constraints before model development
- architect a retrieval-ready knowledge layer for agentic AI systems in cancer research

---

## Introduction

Modern cancer AI does not begin with model architecture. It begins with data ecosystems: interconnected repositories that store genomic variants, transcriptomics, clinical phenotypes, drug response observations, and curated evidence. Strong agentic systems are built on top of these ecosystems, not in isolation from them.

In practice, no single biomedical database is sufficient for end-to-end oncology reasoning. A typical workflow might link TCGA or TARGET cohort-level molecular profiles, cBioPortal or PedcBioPortal study metadata, ClinVar variant assertions, CIViC evidence summaries, and DepMap dependency screens. Each source has different schemas, update cycles, quality standards, and access policies.

This chapter provides a systems-level map of these data sources and shows how to integrate them into robust AI pipelines. The focus is practical: where data comes from, how to normalize it, what can go wrong, and how to expose it safely to agent workflows.

---

## 3.1 Why Biomedical Data Ecosystems Matter for Agentic AI

Agentic AI systems in oncology need more than text generation. They need grounded access to trusted, up-to-date biomedical evidence. Data ecosystems provide this grounding.

### Three Core Roles of the Ecosystem

- evidence retrieval: supplying factual context for model responses
- analytical context: providing cohort and modality information for valid comparisons
- decision traceability: preserving provenance for reproducibility and auditability

### Typical Multi-Source Query Flow

1. detect a molecular entity (for example, a gene variant)
2. retrieve clinical interpretation evidence
3. cross-reference disease context and prevalence
4. connect to therapeutic and functional evidence
5. produce a provenance-linked summary with confidence qualifiers

Without ecosystem-aware retrieval, AI systems may output fluent but unsupported claims. With ecosystem integration, they can produce evidence-linked, inspectable conclusions.

---

## 3.2 Key Data Source Categories

Biomedical repositories can be grouped into complementary categories. Understanding these categories helps define which tool an agent should call for a given subtask.

| Category | Primary Question | Typical Sources |
|---|---|---|
| Population-scale omics cohorts | What molecular patterns exist across tumors? | TCGA, ICGC, GEO |
| Clinical and translational interpretation | How is a variant interpreted in patient care? | ClinVar, OncoKB, CIViC |
| Cancer genomics portals | What does a study report for genes and alterations? | cBioPortal, COSMIC |
| Functional genomics and dependency screens | Is a target biologically actionable in model systems? | DepMap |
| Single-cell and atlas resources | Which cellular states and lineages are involved? | Human Cell Atlas, CELLxGENE |
| Pediatric cancer-specific resources | What child and AYA tumor patterns are represented? | TARGET, St. Jude Cloud, Kids First DRC, PedcBioPortal, OpenPBTA/CBTN |
| Literature and knowledge extraction layers | What supporting studies exist? | PubMed, Europe PMC, curated KGs |

No category is optional for translational AI. Different decisions require different evidence types.

---

## 3.3 Core Oncology Repositories and Their Roles

### TCGA (The Cancer Genome Atlas)

- strength: matched multi-omics with rich tumor subtype coverage
- common use: cohort-level exploration, biomarker discovery, model pretraining data assembly
- caveat: historical pipelines and batch effects require careful harmonization

### GEO (Gene Expression Omnibus)

- strength: broad transcriptomic study coverage, including legacy and rare indications
- common use: external validation and cross-study meta-analysis
- caveat: metadata quality varies across submitters and platforms

### cBioPortal

- strength: study-centric portal and APIs for cancer genomics queries
- common use: cohort prevalence summaries, mutation and copy-number exploration
- caveat: study-specific preprocessing can complicate direct cross-study comparisons

### COSMIC

- strength: curated catalog of somatic mutations across cancers
- common use: recurrence profiling and mutation context enrichment
- caveat: interpretation still requires disease-specific and clinical evidence layers

### ClinVar

- strength: clinically oriented variant assertions with review status metadata
- common use: germline and clinical significance reference checks
- caveat: conflicting assertions can exist across submitters

### CIViC and OncoKB

- strength: expert-curated variant-actionability knowledge
- common use: evidence grading for therapeutic relevance and report generation support
- caveat: evidence levels and update cadence differ; always retain source-specific interpretation

### DepMap

- strength: large-scale CRISPR and pharmacologic dependency screens
- common use: functional prioritization of candidate targets
- caveat: cell-line context may not fully represent patient tumor biology

### Human Cell Atlas

- strength: cell-state-level molecular atlases
- common use: microenvironment context and single-cell reference mapping
- caveat: atlas integration requires ontology and batch harmonization

### Pediatric Cancer Databases and Portals

### TARGET (Therapeutically Applicable Research to Generate Effective Treatments)

- strength: harmonized pediatric cancer genomic and clinical cohorts
- common use: baseline pediatric cohort modeling and cross-cancer comparisons with adult datasets
- caveat: pediatric cohort sizes are smaller and diagnosis-specific distributions are uneven

### St. Jude Cloud

- strength: pediatric-focused genomic data, analysis workflows, and visualization interfaces
- common use: discovery workflows and reproducible analyses for childhood cancer genomics
- caveat: some datasets and workflows require account and governance-aware access planning

### Kids First Data Resource Center (Gabriella Miller Kids First)

- strength: childhood cancer and structural birth defect datasets with cloud-accessible tooling
- common use: pediatric data integration and cross-study cohort assembly
- caveat: phenotypic metadata harmonization can require careful ontology mapping

### PedcBioPortal (Pediatric cBioPortal)

- strength: pediatric oncology portal model with cohort browsing and molecular profiling interfaces
- common use: rapid pediatric cohort prevalence and alteration pattern exploration
- caveat: study-specific processing and release cadence can vary across contributing projects

### CBTN and OpenPBTA Resources

- strength: community-driven pediatric brain tumor resources and reproducible analysis outputs
- common use: pediatric CNS tumor benchmarking, subtype characterization, and translational hypothesis generation
- caveat: controlled-access components and evolving workflows require explicit version tracking

---

## 3.4 Data Modalities and Join Keys

Integrating biomedical data requires explicit join semantics. Misaligned identifiers are a major source of silent errors.

### Common Modalities

- genomic variants: SNVs, indels, structural events
- copy-number and chromosomal alterations
- transcript abundance and isoform-level profiles
- epigenetic or chromatin state signals
- clinical outcomes and treatment timelines
- functional screens and perturbation assays

### Practical Join Keys

- gene identifiers: HGNC symbol, Ensembl gene ID
- variant representation: HGVS and genome build-specific coordinates
- disease terms: standardized ontology mapping (for example, OncoTree, Disease Ontology)
- sample identity: patient ID, aliquot/sample IDs, tissue context
- study identity: accession, release, processing version

Treat identifiers as versioned entities. A gene symbol alone is not a stable universal key.

---

## 3.5 Harmonization Pipeline Design

A robust ingestion pipeline transforms heterogeneous sources into a consistent analysis-ready layer.

### Recommended Pipeline Stages

1. ingestion
2. schema mapping
3. normalization and ontology alignment
4. quality control and anomaly checks
5. provenance tagging and version snapshots
6. persistence into an analytics and retrieval layer

### Minimum Metadata to Preserve

- source database and endpoint
- timestamp and release version
- transformation code version
- license and usage constraints
- confidence and evidence-level fields when available

If provenance is missing, generated outputs cannot be audited or trusted for high-impact use.

---

## 3.6 Data Quality, Bias, and Reproducibility Risks

Data ecosystems contain both biological signal and systematic artifacts. Agents need safeguards against both.

### Frequent Risk Patterns

- cohort composition bias across ancestry, institution, and disease subtype
- low-sample pediatric strata causing unstable estimates and overconfident conclusions
- inconsistent phenotype definitions between studies
- platform and batch effects across sequencing centers
- publication and curation bias favoring well-studied genes
- stale records when local mirrors are not refreshed

### Mitigations for AI Workflows

- stratify and report subgroup coverage before modeling
- report pediatric versus adult cohort boundaries and do not merge labels implicitly
- include metadata-aware filtering in retrieval tools
- store data snapshots and transformation manifests
- attach confidence indicators to downstream summaries
- require citation traceability for each biomedical claim

Reproducible AI in oncology is a data governance problem as much as a modeling problem.

---

## 3.7 Integration Architecture for Agentic Systems

An effective architecture separates raw source connectors from reasoning-time retrieval.

```text
Public Repositories -> Ingestion Connectors -> Harmonization Layer -> Knowledge Store -> Agent Tools -> User-Facing Analysis
```

### Architecture Components

- source connectors: API clients, bulk download handlers, and authentication wrappers
- harmonization layer: schema standardization and ontology normalization
- knowledge store: relational tables, graph relations, and vector indexes
- tool interface: constrained functions for query, filter, and evidence extraction
- policy layer: access control, logging, and human-review triggers

This modular design enables independent updates to data acquisition, storage, and agent behavior.

---

## 3.8 Practical Example: Variant Evidence Aggregation

Consider a task: evaluate a candidate TP53 alteration in a specific tumor context.

### Example Workflow

1. retrieve prevalence from cBioPortal cohorts
2. fetch somatic context from COSMIC
3. check clinical interpretations from ClinVar and CIViC
4. pull actionability level from OncoKB (if licensed and available)
5. summarize with evidence-level labels and source citations

### What a Good Agent Output Should Include

- assertion and confidence statement
- sources used and retrieval timestamps
- evidence disagreements and unresolved conflicts
- clinical-use disclaimer and need for expert review

This pattern scales to many entities, but the same governance principles apply.

---

## 3.9 Designing Retrieval-Ready Biomedical Knowledge Layers

Later RAG and multi-agent chapters depend on this chapter's outputs. A retrieval-ready layer should support both exact and semantic access.

### Storage Pattern Recommendations

- relational layer for structured clinical and molecular facts
- graph layer for gene-disease-therapy-evidence relationships
- vector layer for unstructured evidence passages and study abstracts

### Retrieval Best Practices

- use explicit filters before semantic ranking (disease, tissue, assay, release)
- rank by evidence quality and recency, not only embedding similarity
- return citations and identifiers with every retrieved item
- preserve explainable query plans for debugging and audit

The goal is not maximal retrieval volume. The goal is precise, context-aware evidence access.

---

## 3.10 Preparing for Chapters 4-6

This chapter establishes the data foundation for LLM and RAG workflows:

- Chapter 4 uses these sources to discuss biomedical grounding of language models
- Chapter 5 uses them to design retrieval and citation pipelines
- Chapter 6 applies them to tool-using agents and multi-step evidence workflows

Before moving forward, validate that your environment can do three things reliably:

1. query at least one public oncology API
2. map identifiers and ontologies across two sources
3. return provenance-linked evidence summaries

If these fail, improve data engineering first. Better prompts cannot compensate for weak data plumbing.

---

## Key Takeaways

- Biomedical AI quality is fundamentally constrained by data ecosystem quality.
- Multi-source integration requires explicit schema, identifier, and ontology management.
- Provenance and licensing metadata are first-class requirements, not optional annotations.
- Pediatric oncology integration requires explicit handling of small cohorts, access controls, and age-aware context.
- Retrieval-ready knowledge layers should combine relational, graph, and semantic access.
- Agent outputs must surface uncertainty, evidence levels, and source traceability.

---

## References

- TCGA Program Overview: https://www.cancer.gov/ccg/research/genome-sequencing/tcga
- GEO: https://www.ncbi.nlm.nih.gov/geo/
- cBioPortal: https://www.cbioportal.org/
- COSMIC: https://cancer.sanger.ac.uk/cosmic
- ClinVar: https://www.ncbi.nlm.nih.gov/clinvar/
- CIViC: https://civicdb.org/
- OncoKB: https://www.oncokb.org/
- DepMap: https://depmap.org/portal/
- Human Cell Atlas: https://www.humancellatlas.org/
- TARGET Data Matrix: https://ocg.cancer.gov/programs/target/data-matrix
- St. Jude Cloud: https://platform.stjude.cloud/
- Kids First Data Resource Center: https://kidsfirstdrc.org/
- PedcBioPortal: https://pedcbioportal.org/
- Open Pediatric Brain Tumor Atlas: https://opentargets.github.io/OpenPBTA/

---

## Further Reading

- Grossman RL et al. Toward a Shared Vision for Cancer Genomic Data. N Engl J Med. 2016.
- Kurnit KC et al. Precision oncology decision support in practice. Nat Rev Clin Oncol. 2022.
- Tomczak K et al. The Cancer Genome Atlas (TCGA): an immeasurable source of knowledge. Contemp Oncol. 2015.

