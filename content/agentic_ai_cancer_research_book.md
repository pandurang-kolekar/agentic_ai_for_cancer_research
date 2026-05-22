# Agentic AI for Cancer Research
## Building Intelligent Systems for Computational Biology and Bioinformatics

### A Practical Guide with Theory, Hands-On Labs, and Research Workflows

---

# Front Matter

## Title Page

**Agentic AI for Cancer Research**

Building Intelligent Systems for Computational Biology and Bioinformatics

A Practical Guide with Theory, Case Studies, and Jupyter Notebooks

---

# Preface

Cancer research is entering a new era in which artificial intelligence is evolving from passive analytical tools into active collaborators capable of reasoning, planning, retrieving evidence, orchestrating workflows, and assisting scientific discovery.

This book introduces the foundations and practical implementation of agentic AI systems for computational oncology and bioinformatics. It combines modern AI methods, large language models (LLMs), retrieval systems, knowledge graphs, autonomous workflows, and multi-agent systems with real-world cancer research applications.

The book is designed for:

- Computational biologists
- Cancer researchers
- Bioinformaticians
- Translational scientists
- AI engineers in healthcare
- Graduate students and trainees
- Biomedical informatics professionals

The book emphasizes:

- Scientific rigor
- Reproducibility
- Human-in-the-loop systems
- Explainability
- Safe and responsible AI
- Hands-on implementation

Every chapter includes:

- Theory
- Architecture diagrams
- Visual illustrations
- Biomedical case studies
- Jupyter notebook exercises
- Coding assignments
- Research extensions

---

# Table of Contents

1. Introduction to Agentic AI in Cancer Research
2. Computational Biology Foundations for AI
3. Biomedical Data Ecosystems
4. Large Language Models for Biomedicine
5. Prompt Engineering for Scientific Discovery
6. Retrieval-Augmented Generation in Oncology
7. AI Agents for Genomics and Variant Interpretation
8. Multi-Agent Systems for Biomedical Research
9. Autonomous Bioinformatics Workflow Orchestration
10. Single-Cell and Spatial Omics Agents
11. Knowledge Graphs and Biomedical Reasoning
12. AI for Clinical and Translational Oncology
13. Evaluating Biomedical AI Systems
14. Ethics, Governance, and Responsible AI
15. Building End-to-End Precision Oncology Systems
16. Future Directions in Autonomous Scientific Discovery
17. Capstone Projects and Research Challenges

Appendices:
- Python for Bioinformatics
- APIs and Biomedical Databases
- GPU Infrastructure
- Docker and Reproducibility
- Cloud Deployment
- Notebook Setup Guide

---

# Book Design Standards

## Graphics Style

The book should use:

- Clean scientific diagrams
- Workflow architecture schematics
- Biological pathway illustrations
- AI agent interaction maps
- Knowledge graph visualizations
- Genomics pipeline diagrams
- Flowcharts for decision systems
- Multimodal biomedical AI illustrations

## Suggested Color Palette

- Deep blue for AI components
- Green for biological systems
- Orange for clinical systems
- Gray for infrastructure
- Purple for knowledge graphs

## Recommended Figure Types

| Figure Type | Example |
|---|---|
| Workflow diagrams | Multi-agent orchestration |
| Architecture diagrams | RAG pipeline |
| Genomics schematics | Variant interpretation workflow |
| Knowledge graphs | Gene-drug-disease networks |
| Statistical plots | Survival analysis |
| Embedding visualizations | UMAP/t-SNE |
| Decision trees | Clinical reasoning |
| Timelines | Drug resistance evolution |

---

# Chapter 1
# Introduction to Agentic AI in Cancer Research

## Learning Objectives

By the end of this chapter, readers will:

- Understand agentic AI concepts
- Distinguish AI agents from workflows and copilots
- Learn applications in cancer research
- Understand limitations and risks
- Build a simple biomedical AI assistant

---

# Section 1.1 — What Is Agentic AI?

Agentic AI refers to systems capable of:

- Planning tasks
- Making decisions
- Using tools
- Accessing memory
- Retrieving information
- Coordinating workflows
- Iteratively improving outputs

Unlike static predictive systems, agentic AI systems act dynamically within an environment.

## Figure 1.1 — Evolution of AI Systems

```text
Rule-Based Systems
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
Foundation Models
        ↓
Agentic AI Systems
```

### Graphic Description
A layered evolution diagram showing progression from rule-based systems to autonomous biomedical AI agents.

---

# Section 1.2 — Why Agentic AI Matters in Cancer Research

Modern cancer research involves:

- Massive multimodal datasets
- Thousands of publications weekly
- Complex molecular interactions
- High-dimensional omics data
- Translational decision making

AI agents can help:

- Automate analyses
- Retrieve evidence
- Generate hypotheses
- Coordinate workflows
- Interpret variants
- Summarize literature
- Assist tumor boards

---

# Figure 1.2 — Agentic AI in Precision Oncology

```text
Patient Data
   ↓
AI QC Agent
   ↓
Variant Interpretation Agent
   ↓
Literature Retrieval Agent
   ↓
Clinical Trial Matching Agent
   ↓
Tumor Board Summary Agent
```

### Graphic Recommendation
A clinical precision oncology workflow diagram with interacting AI agents.

---

# Section 1.3 — Core Components of AI Agents

## Planning
Determining task sequences.

## Memory
Maintaining context and historical information.

## Tool Use
Calling external systems:

- PubMed
- BLAST
- GATK
- ClinicalTrials.gov
- Knowledge graphs

## Reflection
Evaluating and correcting outputs.

## Retrieval
Searching biomedical literature and databases.

---

# Figure 1.3 — Anatomy of an AI Agent

```text
+----------------+
|     User       |
+----------------+
         ↓
+----------------+
|  Planner       |
+----------------+
         ↓
+----------------+
| Tool Executor  |
+----------------+
         ↓
+----------------+
| Memory System  |
+----------------+
         ↓
+----------------+
| Reflection     |
+----------------+
```

---

# Hands-On Notebook 1
# Building a Biomedical Research Assistant

## Notebook Goals

Participants build an AI assistant that:

- Retrieves PubMed abstracts
- Summarizes findings
- Suggests analyses
- Answers oncology questions

---

# Notebook Structure

## Section A — Setup

```python
pip install langchain openai biopython pymed pandas
```

---

## Section B — PubMed Retrieval

```python
from pymed import PubMed

pubmed = PubMed(tool="CancerResearchAI", email="user@example.com")

query = "triple negative breast cancer biomarkers"
results = pubmed.query(query, max_results=5)

for article in results:
    print(article.title)
```

---

## Section C — LLM Summarization

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a cancer biology assistant."},
        {"role": "user", "content": "Summarize TNBC biomarkers."}
    ]
)

print(response.choices[0].message.content)
```

---

## Section D — Structured Output

Generate:

- Biomarkers
- Pathways
- Therapeutic targets
- Experimental recommendations

---

# Case Study 1
# Triple-Negative Breast Cancer Biomarker Discovery

## Research Question

Which biomarkers are associated with treatment resistance in TNBC?

## Tasks

- Retrieve literature
- Identify candidate genes
- Perform pathway enrichment
- Build evidence summary

## Suggested Datasets

- TCGA BRCA
- GEO TNBC datasets

---

# Chapter 2
# Computational Biology Foundations for AI

## Topics

- DNA/RNA/protein fundamentals
- Central dogma
- Genomics workflows
- Transcriptomics
- Proteomics
- Single-cell biology
- Spatial omics

---

# Figure 2.1 — Multi-Omics Landscape

```text
Genomics
    ↓
Transcriptomics
    ↓
Proteomics
    ↓
Phenotype
```

---

# Hands-On Notebook 2
# Exploring TCGA Data

## Goals

- Access TCGA datasets
- Analyze mutations
- Visualize expression profiles
- Perform survival analysis

---

## Example Code

```python
import pandas as pd

clinical = pd.read_csv("clinical.tsv", sep="\t")
expression = pd.read_csv("expression.tsv", sep="\t")

print(clinical.head())
```

---

## Visualization Exercise

```python
import matplotlib.pyplot as plt

plt.hist(clinical['days_to_death'].dropna())
plt.xlabel('Days to Death')
plt.ylabel('Patients')
plt.title('Survival Distribution')
plt.show()
```

---

# Chapter 3
# Biomedical Data Ecosystems

## Topics

- TCGA
- GEO
- cBioPortal
- COSMIC
- ClinVar
- CIViC
- OncoKB
- DepMap
- Human Cell Atlas

---

# Figure 3.1 — Biomedical Data Integration Architecture

```text
Public Databases
        ↓
Data Harmonization
        ↓
Knowledge Layer
        ↓
AI Agent Layer
        ↓
Scientific Applications
```

---

# Hands-On Notebook 3
# cBioPortal API Integration

## Objectives

- Query mutation profiles
- Retrieve cohorts
- Visualize molecular alterations

---

## Example Code

```python
import requests

url = "https://www.cbioportal.org/api/studies"
response = requests.get(url)

print(response.json()[:3])
```

---

# Chapter 4
# Large Language Models for Biomedicine

## Topics

- Transformers
- Attention mechanisms
- Biomedical foundation models
- Fine-tuning
- Hallucinations
- Tool calling

---

# Figure 4.1 — Transformer Architecture

### Graphic Description
Illustration of token embeddings, self-attention, and transformer blocks.

---

# Hands-On Notebook 4
# Prompt Engineering for Bioinformatics

## Exercises

- Variant interpretation prompts
- Experimental design prompts
- Literature summarization prompts
- Structured extraction prompts

---

## Example Prompt

```python
prompt = """
You are an oncology genomics expert.

Interpret the following TP53 mutation:
R273H

Provide:
1. Functional impact
2. Known cancer associations
3. Therapeutic implications
4. Supporting evidence
"""
```

---

# Chapter 5
# Retrieval-Augmented Generation in Oncology

## Topics

- Semantic search
- Embeddings
- Vector databases
- Citation grounding
- Biomedical retrieval systems

---

# Figure 5.1 — RAG Pipeline

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retriever
   ↓
LLM Generator
```

---

# Hands-On Notebook 5
# Building a Biomedical RAG System

## Objectives

- Ingest PubMed papers
- Generate embeddings
- Build vector search
- Create evidence-grounded QA

---

## Example Code

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode([
    "KRAS mutations are common in pancreatic cancer"
])
```

---

# Chapter 6
# AI Agents for Genomics

## Topics

- Variant calling
- Functional annotation
- RNA-seq automation
- Pipeline orchestration
- Autonomous QC

---

# Figure 6.1 — Variant Interpretation Workflow

```text
VCF Input
   ↓
Annotation
   ↓
Pathogenicity Scoring
   ↓
Literature Evidence
   ↓
Clinical Interpretation
```

---

# Hands-On Notebook 6
# Variant Annotation Agent

## Tasks

- Read VCF files
- Query ClinVar
- Query COSMIC
- Generate reports

---

## Example Code

```python
import pandas as pd

vcf = pd.read_csv("variants.vcf", comment="#", sep="\t")

print(vcf.head())
```

---

# Case Study
# Lung Adenocarcinoma Precision Oncology

## Scenario

A patient presents with:

- EGFR mutation
- Acquired resistance
- RNA-seq expression changes

## Tasks

- Identify driver mutations
- Evaluate resistance pathways
- Suggest clinical trials

---

# Chapter 7
# Multi-Agent Systems for Biomedical Discovery

## Topics

- Planner agents
- Executor agents
- Reflection agents
- Critic systems
- Memory architectures
- Collaborative scientific reasoning

---

# Figure 7.1 — Multi-Agent Collaboration

```text
Literature Agent
        ↕
Genomics Agent
        ↕
Clinical Agent
        ↕
Report Agent
```

---

# Hands-On Notebook 7
# Building a Multi-Agent Cancer Research System

## Agents

- Literature retrieval agent
- Differential expression agent
- Statistical analysis agent
- Clinical summarization agent

---

## Frameworks

- AutoGen
- CrewAI
- LangGraph

---

# Chapter 8
# Autonomous Workflow Orchestration

## Topics

- Nextflow
- Snakemake
- Docker
- Kubernetes
- Workflow provenance
- Human oversight

---

# Figure 8.1 — Autonomous Bioinformatics Workflow

```text
Data Ingestion
      ↓
QC Agent
      ↓
Analysis Agent
      ↓
Visualization Agent
      ↓
Reporting Agent
```

---

# Hands-On Notebook 8
# Automated RNA-seq Analysis

## Workflow

- FASTQ QC
- Alignment
- Quantification
- Differential expression
- Pathway enrichment

---

# Example Nextflow Snippet

```nextflow
process FASTQC {
    input:
    path reads

    output:
    path "*.html"

    script:
    """
    fastqc ${reads}
    """
}
```

---

# Chapter 9
# Single-Cell and Spatial Omics Agents

## Topics

- Cell clustering
- Cell annotation
- Spatial transcriptomics
- Cell-cell interaction analysis
- AI-guided annotation

---

# Figure 9.1 — Single-Cell Workflow

```text
Raw Counts
   ↓
Normalization
   ↓
Dimensionality Reduction
   ↓
Clustering
   ↓
Cell Annotation
```

---

# Hands-On Notebook 9
# Single-Cell Tumor Microenvironment Analysis

## Tasks

- UMAP visualization
- Cell type annotation
- Differential expression
- Immune profiling

---

## Example Code

```python
import scanpy as sc

adata = sc.read_h5ad("tumor_data.h5ad")

sc.pp.normalize_total(adata)
sc.tl.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)

sc.pl.umap(adata, color='cell_type')
```

---

# Chapter 10
# Knowledge Graphs and Biomedical Reasoning

## Topics

- Neo4j
- GraphRAG
- Ontologies
- Gene-drug-disease networks
- Symbolic reasoning

---

# Figure 10.1 — Cancer Knowledge Graph

```text
Gene → Pathway → Disease → Drug → Clinical Trial
```

---

# Hands-On Notebook 10
# Building a Biomedical Knowledge Graph

## Tasks

- Create nodes
- Build relationships
- Query pathways
- Generate hypotheses

---

## Example Cypher Query

```cypher
MATCH (g:Gene)-[:ASSOCIATED_WITH]->(d:Disease)
WHERE d.name = 'Glioblastoma'
RETURN g
```

---

# Chapter 11
# AI for Clinical and Translational Oncology

## Topics

- Clinical trial matching
- Molecular tumor boards
- Temporal reasoning
- Real-world evidence
- EHR integration

---

# Figure 11.1 — Molecular Tumor Board AI Architecture

### Graphic Description
A layered architecture showing clinical records, molecular profiles, AI reasoning agents, and physician oversight.

---

# Hands-On Notebook 11
# Clinical Trial Matching Agent

## Tasks

- Parse molecular profiles
- Match eligibility criteria
- Rank relevant trials

---

# Chapter 12
# Evaluating Biomedical AI Systems

## Topics

- Hallucination detection
- Retrieval evaluation
- Clinical reliability
- Scientific reproducibility
- Benchmarking

---

# Figure 12.1 — Biomedical AI Evaluation Framework

```text
Accuracy
   +
Grounding
   +
Explainability
   +
Reproducibility
   +
Safety
```

---

# Hands-On Notebook 12
# AI Agent Evaluation Pipeline

## Tasks

- Evaluate factual consistency
- Measure retrieval precision
- Assess hallucinations
- Compare outputs against experts

---

# Chapter 13
# Ethics and Responsible AI

## Topics

- Bias
- Privacy
- Security
- FDA considerations
- Explainability
- Human oversight
- Safe deployment

---

# Figure 13.1 — Responsible Biomedical AI Principles

```text
Transparency
Fairness
Safety
Accountability
Privacy
Human Oversight
```

---

# Chapter 14
# Building an End-to-End Precision Oncology System

## Integrated Capstone

Participants build:

- Data ingestion systems
- Variant interpretation agents
- RAG literature systems
- Clinical trial matching systems
- Tumor board summarization

---

# Figure 14.1 — End-to-End Precision Oncology Platform

```text
Sequencing Data
      ↓
Genomics Agent
      ↓
Knowledge Graph Agent
      ↓
Literature RAG
      ↓
Clinical Trial Matching
      ↓
Tumor Board Report
```

---

# Capstone Projects

## Project 1 — AI Molecular Tumor Board

### Deliverables

- Agent architecture
- Variant interpretation
- Evidence retrieval
- Trial recommendations

---

## Project 2 — Autonomous Single-Cell Discovery Platform

### Deliverables

- Cell annotation
- Pathway analysis
- Immune profiling
- Automated reporting

---

## Project 3 — Drug Repurposing Agent

### Deliverables

- Knowledge graph
- Mechanistic reasoning
- Candidate ranking
- Evidence reports

---

# Appendix A
# Jupyter Notebook Setup

## Recommended Environment

```bash
conda create -n cancer-ai python=3.11
conda activate cancer-ai
```

---

## Install Dependencies

```bash
pip install \
langchain \
llama-index \
openai \
pandas \
numpy \
scanpy \
biopython \
matplotlib \
scikit-learn \
sentence-transformers \
chromadb \
neo4j \
jupyterlab
```

---

# Appendix B
# Recommended Repository Structure

```text
book/
├── chapters/
├── figures/
├── notebooks/
├── datasets/
├── docker/
├── workflows/
├── slides/
└── solutions/
```

---

# Appendix C
# Suggested Graphics Package

## Recommended Tools

- BioRender
- draw.io
- Mermaid diagrams
- Cytoscape
- Adobe Illustrator
- Graphviz
- Plotly
- Matplotlib

---

# Appendix D
# Suggested Notebook List

| Notebook | Topic |
|---|---|
| notebook_01_intro.ipynb | Biomedical AI assistant |
| notebook_02_tcga.ipynb | TCGA exploration |
| notebook_03_prompt_engineering.ipynb | Scientific prompts |
| notebook_04_rag.ipynb | Biomedical RAG |
| notebook_05_variant_agent.ipynb | Variant interpretation |
| notebook_06_multiagent.ipynb | Multi-agent systems |
| notebook_07_rnaseq.ipynb | RNA-seq workflows |
| notebook_08_singlecell.ipynb | Single-cell analysis |
| notebook_09_knowledge_graph.ipynb | Neo4j biomedical graphs |
| notebook_10_clinical_trials.ipynb | Trial matching |
| notebook_11_evaluation.ipynb | Agent benchmarking |
| notebook_12_capstone.ipynb | Integrated precision oncology |

---

# Part I — Foundations of Agentic AI in Cancer Research

---

# Chapter 1 — Introduction to Agentic AI in Cancer Research

## Chapter Overview

Cancer research increasingly depends on the integration of large-scale biomedical data, computational workflows, and translational decision-making systems. Traditional computational approaches often require substantial manual intervention, fragmented tooling, and extensive domain expertise to coordinate analyses.

Agentic artificial intelligence introduces a paradigm shift in which AI systems move beyond passive prediction and become active computational collaborators capable of:

- Planning
- Tool orchestration
- Multi-step reasoning
- Evidence retrieval
- Scientific summarization
- Workflow automation
- Reflection and self-correction

In oncology, these systems can assist researchers in managing the complexity of:

- Multi-omics datasets
- Rapidly evolving literature
- Clinical interpretation pipelines
- Drug resistance analysis
- Biomarker discovery
- Translational research workflows

This chapter introduces the conceptual foundations of agentic AI and explores why these systems are particularly important in computational oncology.

---

## Learning Objectives

After completing this chapter, readers should be able to:

1. Define agentic AI.
2. Differentiate agents from conventional machine learning systems.
3. Explain core architectural components of AI agents.
4. Describe applications in cancer research.
5. Understand limitations and safety concerns.
6. Build a basic biomedical research assistant.

---

# 1.1 The Evolution of AI Systems

Artificial intelligence systems have evolved through multiple generations of computational paradigms.

## Rule-Based Systems

Early biomedical systems relied on manually encoded rules:

```text
IF mutation = EGFR
AND exon = 19 deletion
THEN suggest EGFR inhibitor
```

Although interpretable, rule-based systems struggled with:

- Scalability
- Ambiguity
- Novel discoveries
- Complex molecular interactions

## Statistical Machine Learning

Machine learning introduced probabilistic modeling approaches:

- Logistic regression
- Random forests
- Support vector machines
- Bayesian systems

These methods enabled prediction but still depended heavily on feature engineering.

## Deep Learning

Deep learning transformed computational biology through:

- Representation learning
- Automated feature extraction
- Large-scale modeling
- Multimodal integration

Applications included:

- Histopathology classification
- Variant calling
- Protein structure prediction
- Drug response prediction

## Foundation Models

Large-scale transformer architectures enabled:

- Generalized language understanding
- Cross-domain transfer learning
- Scientific reasoning capabilities
- Tool integration

Biomedical foundation models include:

- BioGPT
- PubMedBERT
- Med-PaLM
- BioMedLM

## Agentic AI

Agentic AI systems extend foundation models by integrating:

- Planning systems
- Tool execution
- Long-term memory
- Retrieval systems
- Multi-agent collaboration
- Autonomous workflows

These systems behave more like research collaborators than static predictors.

---

# Figure 1.1 — Evolution of Biomedical AI

```text
Rule-Based Systems
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
Foundation Models
        ↓
Agentic AI Systems
```

---

# 1.2 Defining Agentic AI

Agentic AI refers to systems capable of autonomous or semi-autonomous behavior while pursuing specified objectives.

Unlike conventional AI systems that perform isolated predictions, agents can:

- Interpret goals
- Plan actions
- Interact with environments
- Use computational tools
- Retrieve external information
- Adapt workflows dynamically
- Evaluate their own outputs

In biomedical research, this means agents can potentially:

- Retrieve literature from PubMed
- Execute bioinformatics workflows
- Analyze RNA-seq datasets
- Interpret genomic variants
- Generate scientific reports
- Coordinate multi-step analyses

---

# 1.3 Why Cancer Research Needs Agentic AI

Modern cancer research generates enormous quantities of heterogeneous data.

## Major Challenges

### 1. Data Volume

Large-scale cancer projects generate:

- Whole-genome sequencing
- RNA-seq
- Single-cell transcriptomics
- Spatial omics
- Proteomics
- Clinical metadata

### 2. Literature Explosion

Thousands of oncology papers are published every week.

Researchers struggle to:

- Stay current
- Integrate evidence
- Compare findings
- Identify contradictions

### 3. Translational Complexity

Precision oncology requires integration across:

- Molecular biology
- Clinical medicine
- Pharmacology
- Genomics
- Statistical modeling

### 4. Reproducibility

Many computational analyses remain difficult to reproduce due to:

- Pipeline fragmentation
- Inconsistent metadata
- Tool incompatibility
- Manual processing steps

Agentic AI systems can help address these limitations.

---

# 1.4 Core Components of AI Agents

## Planning

Planning systems determine:

- Task decomposition
- Execution ordering
- Dependency management
- Iterative refinement

Example:

```text
Goal:
Identify therapeutic targets in melanoma.

Plan:
1. Retrieve datasets
2. Run differential expression
3. Perform pathway analysis
4. Retrieve literature evidence
5. Rank targets
6. Generate report
```

---

## Memory

Memory systems allow agents to retain:

- Previous actions
- Intermediate results
- User preferences
- Historical evidence

### Types of Memory

| Memory Type | Example |
|---|---|
| Short-term | Current conversation |
| Long-term | Prior analyses |
| Vector memory | Embedding retrieval |
| Structured memory | Databases and graphs |

---

## Tool Use

Agents become significantly more powerful when they can execute external tools.

### Biomedical Tool Examples

| Tool | Purpose |
|---|---|
| PubMed API | Literature retrieval |
| BLAST | Sequence alignment |
| GATK | Variant calling |
| Scanpy | Single-cell analysis |
| Neo4j | Knowledge graph querying |
| ClinicalTrials.gov | Trial matching |

---

## Reflection

Reflection enables agents to:

- Detect mistakes
- Validate outputs
- Re-plan tasks
- Improve reliability

Example:

```text
Initial output:
Low-confidence variant interpretation.

Reflection step:
Retrieve additional ClinVar evidence.
```

---

## Retrieval

Retrieval systems enable access to external knowledge sources.

In biomedical AI, retrieval is essential because:

- Scientific evidence changes rapidly
- Static models become outdated
- Citation grounding is critical

Retrieval-Augmented Generation (RAG) systems help mitigate hallucinations.

---

# 1.5 AI Agents vs Traditional Pipelines

| Feature | Traditional Pipeline | Agentic System |
|---|---|---|
| Fixed workflow | Yes | No |
| Dynamic planning | No | Yes |
| Tool orchestration | Limited | Extensive |
| Self-correction | Minimal | Possible |
| Interactive reasoning | No | Yes |
| Human collaboration | Limited | Extensive |

---

# 1.6 Biomedical Use Cases

## Literature Mining

Agents can:

- Summarize evidence
- Extract biomarkers
- Identify therapeutic targets
- Compare studies

## Variant Interpretation

Agents can:

- Query ClinVar
- Retrieve COSMIC annotations
- Rank pathogenicity
- Generate reports

## Single-Cell Analysis

Agents can automate:

- QC
- Clustering
- Cell annotation
- Pathway enrichment

## Clinical Trial Matching

Agents can:

- Parse molecular profiles
- Match inclusion criteria
- Rank candidate trials

---

# 1.7 Limitations of Agentic Biomedical AI

Despite their potential, agentic systems have important limitations.

## Hallucinations

LLMs may generate incorrect biomedical claims.

## Evidence Reliability

Retrieved literature may:

- Conflict
- Be outdated
- Lack reproducibility

## Clinical Safety

Incorrect recommendations may create patient risk.

## Computational Cost

Multi-agent systems may require:

- GPUs
- Large memory
- Distributed infrastructure

## Regulatory Constraints

Clinical deployment may require:

- Validation
- Auditing
- Governance frameworks

---

# 1.8 Human-in-the-Loop AI

Biomedical AI systems should augment—not replace—experts.

Human oversight remains essential for:

- Clinical interpretation
- Scientific validation
- Ethical decision-making
- Experimental design

A recommended design principle is:

```text
AI-assisted, human-supervised oncology workflows.
```

---

# Hands-On Notebook 1
# Building a Biomedical Research Assistant

## Objectives

Readers will:

- Access PubMed literature
- Use an LLM for summarization
- Build a simple biomedical assistant
- Generate evidence-grounded outputs

---

## Notebook Environment Setup

```bash
pip install langchain openai pymed pandas matplotlib
```

---

## Step 1 — Retrieve PubMed Articles

```python
from pymed import PubMed

pubmed = PubMed(tool="CancerAI", email="researcher@example.com")

query = "triple negative breast cancer biomarkers"
results = pubmed.query(query, max_results=5)

articles = []

for article in results:
    articles.append({
        "title": article.title,
        "abstract": article.abstract
    })

articles[:2]
```

---

## Step 2 — Summarize Findings Using an LLM

```python
from openai import OpenAI

client = OpenAI()

context = "
".join([
    a["abstract"] for a in articles if a["abstract"]
])

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are an oncology research assistant."
        },
        {
            "role": "user",
            "content": f"Summarize biomarkers discussed here:
{context}"
        }
    ]
)

print(response.choices[0].message.content)
```

---

## Step 3 — Structured Biomedical Extraction

```python
prompt = """
Extract:
1. Biomarkers
2. Pathways
3. Therapeutic targets
4. Experimental recommendations
"""
```

---

# Case Study — Triple-Negative Breast Cancer

## Scenario

Researchers want to identify biomarkers associated with therapy resistance in triple-negative breast cancer (TNBC).

## Tasks

1. Retrieve literature.
2. Identify recurrent biomarkers.
3. Build pathway summaries.
4. Generate candidate hypotheses.

## Suggested Extensions

- Integrate TCGA BRCA expression data
- Perform differential expression
- Build a TNBC knowledge graph
- Compare immunotherapy response signatures

---

# Key Takeaways

In this chapter, readers learned:

- Foundations of agentic AI
- Core components of AI agents
- Applications in computational oncology
- Biomedical use cases
- Risks and limitations
- Initial implementation strategies

The next chapter introduces computational biology foundations necessary for building reliable biomedical AI systems.

---

# Exercises

## Conceptual Questions

1. What distinguishes an AI agent from a traditional machine learning model?
2. Why is retrieval essential in biomedical AI?
3. What are major risks associated with autonomous oncology systems?

## Practical Exercises

1. Modify the PubMed query to focus on glioblastoma.
2. Build a structured extraction prompt for immunotherapy biomarkers.
3. Add citation tracking to the assistant.

---

# Suggested Reading

- ReAct: Synergizing Reasoning and Acting in Language Models
- BioGPT
- PubMedBERT
- The Cancer Genome Atlas publications
- Precision oncology review articles

---

# Final Notes

This book is intended to serve as:

- A graduate-level textbook
- A professional training manual
- A workshop companion
- A translational oncology AI guide
- A computational biology reference

The integration of agentic AI with computational oncology represents one of the most transformative opportunities in biomedical research. The future of precision medicine will likely depend on collaborative intelligence between human experts and trustworthy AI agents capable of accelerating discovery while maintaining scientific rigor and clinical responsibility.

