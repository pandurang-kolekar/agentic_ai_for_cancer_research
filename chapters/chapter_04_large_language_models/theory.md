# Chapter 04: Large Language Models for Biomedicine

## Learning Objectives

By the end of this chapter, you will:

- explain how transformer-based language models represent and generate biomedical text
- distinguish general-purpose foundation models from biomedical-adapted LLMs and domain-tuned variants
- identify where LLMs help in oncology workflows and where they introduce serious failure risk
- design prompts, structured outputs, and tool-calling patterns that improve scientific reliability
- evaluate biomedical LLM outputs for factual grounding, calibration, and downstream usefulness
- connect LLM components to later chapters on retrieval, agents, and clinical translation

---

## Introduction

Large language models (LLMs) are now central to many biomedical AI systems because they can translate between human scientific language and machine-executable workflows. In oncology, this makes them useful for tasks such as literature triage, evidence summarization, structured extraction, cohort annotation, and natural-language interfaces over genomics tools.

However, strong fluency is not the same thing as scientific validity. Biomedical language contains dense abbreviations, overloaded gene symbols, shifting disease terminology, and claims whose correctness depends on tumor type, assay modality, and evidence level. An LLM can sound authoritative while silently mixing these contexts. In cancer research, that is not a cosmetic error. It can distort interpretation, misstate mechanism, or encourage the wrong follow-up analysis.

This chapter treats LLMs as components in a rigorous biomedical system, not as standalone oracles. The goal is to understand how they work, why biomedical adaptation matters, where they fail, and how to constrain them so they can support agentic workflows safely.

---

## 4.1 What Makes LLMs Different From Earlier NLP Systems

Earlier biomedical NLP pipelines usually depended on task-specific feature engineering, named-entity dictionaries, or smaller sequence models trained for one benchmark at a time. LLMs differ because they learn broad language representations from large corpora and can be adapted to many tasks through prompting, fine-tuning, retrieval, and tool use.

### Capabilities That Matter in Biomedicine

- semantic summarization across heterogeneous evidence sources
- few-shot adaptation to new documentation or extraction tasks
- structured generation for reports, tables, and JSON records
- multi-step reasoning over protocols, variants, pathways, and trial criteria
- natural-language interfaces to databases, code tools, and workflow engines

### Why This Is Useful for Cancer Research

Cancer research teams work across publications, cohort tables, pathology descriptions, genomic annotations, and clinical notes. LLMs are valuable because they can mediate between these representations. For example, they can transform a free-text variant note into a structured evidence record or help map an analyst's intent into a retrieval query over a biomedical knowledge base.

The key phrase is mediate, not replace. The model should sit between users and validated evidence systems, not in front of them as a substitute for evidence.

---

## 4.2 Transformer Foundations

Most modern LLMs are based on the transformer architecture. The core innovation is self-attention, which allows a model to decide which earlier or surrounding tokens are most relevant when computing a representation for the current token.

### High-Level Transformer Flow

1. tokenize text into subword or byte-level units
2. convert tokens into learned embeddings
3. add positional information so order is represented
4. apply repeated attention and feed-forward blocks
5. generate probability distributions over the next token or masked token targets

### Why Attention Matters

In biomedical text, meaning often depends on long-range dependencies. Consider a paragraph where a mutation is introduced in one sentence, the tumor type is mentioned later, and therapeutic relevance appears in a final clause. Attention helps connect these elements without the strict locality limitations of older recurrent models.

For a sequence of queries $Q$, keys $K$, and values $V$, scaled dot-product attention is:

$$
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

You do not need to compute this manually in practice, but you do need to understand its implication: the model is continuously reweighting context to build token-level meaning.

### Biomedical Relevance of Tokenization

Tokenization is not trivial in this domain. Strings such as `BRAF V600E`, `ERBB2-amplified`, `PD-L1`, or `c.35G>T` do not behave like ordinary consumer-language phrases. If tokenization fragments these patterns poorly, the model may learn weaker representations or mis-handle structured biomedical language. This is one reason domain adaptation matters.

---

## 4.3 Pretraining, Adaptation, and Biomedical Specialization

A general LLM is trained on broad internet or mixed-text corpora. A biomedical LLM is usually adapted using one or more of the following strategies:

- continued pretraining on PubMed, PMC, textbooks, protocols, or EHR-adjacent text
- supervised fine-tuning on biomedical instruction datasets
- preference optimization for domain-specific response style and caution
- retrieval augmentation over scientific corpora and knowledge bases
- tool calling to external evidence systems rather than memorizing facts

### Why Domain Adaptation Helps

Biomedical writing differs from general web text in several ways:

- terminology is denser and more ambiguous
- evidence quality is uneven and context-dependent
- claims often require explicit citation or level-of-evidence qualifiers
- abbreviations can be unsafe without local disambiguation
- rare diseases and pediatric subtypes are underrepresented in generic corpora

Domain-adapted models often improve on entity recognition, relation extraction, question answering, and summarization benchmarks. More importantly, they usually improve the model's ability to remain within biomedical discourse conventions. That does not mean they become automatically trustworthy. It means the baseline failure rate can be reduced before additional safeguards are added.

### General vs Biomedical LLMs

| Model Category | Strength | Limitation |
|---|---|---|
| General foundation model | Broad reasoning and strong instruction following | May miss biomedical nuance or overgeneralize |
| Biomedical-adapted LLM | Better domain vocabulary and evidence style | Can still hallucinate and may lag latest evidence |
| Institution-tuned model | Better fit to local tasks and formats | Narrow scope and higher maintenance burden |

In practice, many strong biomedical systems combine a capable general model with retrieval, structured prompting, and domain-specific tools rather than relying on a domain model alone.

---

## 4.4 Core Biomedical Use Cases

LLMs are most useful when they reduce cognitive overhead around already-existing evidence or workflows.

### Common High-Value Tasks

- literature triage and evidence summarization
- structured extraction from abstracts, reports, or trial descriptions
- ontology-aware normalization of disease and biomarker terms
- report drafting for variant interpretation or cohort analysis
- natural-language query interfaces over internal data products
- agent planning and routing for multi-tool biomedical workflows

### Oncology Examples

- convert free-text molecular pathology notes into structured mutation tables
- summarize evidence for a candidate resistance mechanism across papers
- generate retrieval queries for tumor-specific biomarker search
- draft a trial matching rationale that must then be verified against source eligibility criteria

These are augmentation tasks. The model accelerates synthesis, but the system should preserve source attribution and explicit review steps.

---

## 4.5 Hallucinations, Miscalibration, and Domain Failure Modes

Biomedical LLM failures are often subtle. They do not always appear as obvious nonsense. More commonly, they appear as plausible but unsupported claims.

### Frequent Failure Patterns

- invented citations or inaccurate attribution to real papers
- mutation interpretation stated without tumor-type context
- adult evidence incorrectly transferred to pediatric disease
- confusion between prognostic, predictive, and diagnostic evidence
- overstated mechanism from correlational literature
- omission of uncertainty when evidence is conflicting or sparse
- fabricated numerical results, cohorts, or trial identifiers

### Why Hallucinations Are Dangerous in Cancer Research

Biomedical decisions are path-dependent. A wrong summary can alter what evidence is reviewed next, what experiment is run, or which case is escalated. Even when the final human reviewer catches the mistake, the LLM may already have biased the workflow.

### Practical Mitigations

- require source-linked answers instead of free-form assertions
- constrain outputs to schemas with explicit fields for evidence and uncertainty
- separate extraction from interpretation rather than asking for both at once
- use retrieval or tool calls for current facts, trial data, and curated knowledge
- treat low-support answers as escalation cases, not completed outputs

If an LLM produces biomedical claims without traceable evidence, the system design is incomplete.

---

## 4.6 Prompt Design for Scientific Work

Prompting matters because it controls task framing, not because it magically creates expertise. In biomedicine, a good prompt narrows the action space and forces the model to expose assumptions.

### Productive Prompt Elements

- a precise role scoped to the task, such as extractor, summarizer, or routing assistant
- explicit input context, including tumor type, assay, and question type
- output schema or JSON format
- instructions to distinguish evidence from inference
- uncertainty handling rules and escalation criteria

### Example Prompt Pattern

```text
You are assisting with oncology evidence extraction.

Task:
- Extract only claims directly supported by the provided text.
- Do not add external facts.
- If support is missing, return "insufficient_evidence".

Return JSON with:
- gene
- alteration
- tumor_type
- evidence_statement
- confidence
- unsupported_claims_detected
```

This prompt is better than a generic “interpret this mutation” instruction because it narrows the model to extraction and forces structured output.

### Prompting Is Not a Substitute for Grounding

Careful prompts reduce variance, but they do not solve missing evidence, outdated knowledge, or benchmark mismatch. Prompt quality is one layer in a multi-layer reliability stack.

---

## 4.7 Tool Calling and Retrieval as Reliability Mechanisms

For high-stakes biomedical tasks, LLMs should usually operate with tools. Tool calling shifts the system from “answer from parametric memory” toward “retrieve or compute before answering.”

### Common Biomedical Tools for LLM Systems

- PubMed or Europe PMC search
- cBioPortal and related cohort APIs
- ClinVar, CIViC, or knowledge-base lookup tools
- ontology mappers and normalization services
- Python analysis tools for tabular or statistical summaries

### Typical Tool-Augmented Flow

1. classify the user request
2. choose the appropriate evidence source or computational tool
3. retrieve or compute structured results
4. summarize outputs with citations and caveats
5. escalate to human review when evidence is weak or conflicting

This pattern is essential for later chapters on retrieval-augmented generation, genomics agents, and clinical decision support.

---

## 4.8 Fine-Tuning and Instruction Tuning

Fine-tuning can improve consistency on narrow biomedical tasks, but it introduces maintenance and governance overhead.

### When Fine-Tuning Helps

- repeated structured extraction tasks with stable schemas
- institution-specific report formats
- constrained reasoning styles that must remain consistent across many runs
- internal datasets with terminology not handled well by public models

### When Fine-Tuning Is the Wrong First Move

- when the main issue is missing or outdated evidence
- when tasks are better solved with retrieval and schema constraints
- when the domain changes rapidly and static knowledge becomes stale
- when labeled data is sparse or weakly curated

Many teams fine-tune too early. In biomedical settings, retrieval, prompt design, and workflow constraints often deliver better reliability-per-effort than custom model tuning.

---

## 4.9 Evaluation of Biomedical LLMs

Evaluating LLMs for biomedicine is not the same as measuring generic chatbot quality. A useful evaluation framework should test whether the model is correct, grounded, calibrated, and operationally safe.

### Important Evaluation Dimensions

- factual accuracy against trusted references
- citation fidelity and evidence alignment
- structured-output validity
- uncertainty calibration and refusal behavior
- robustness across tumor types, rare entities, and pediatric settings
- usefulness in real analyst workflows

### Useful Task Families

| Task Family | What to Measure |
|---|---|
| Extraction | field accuracy, omission rate, JSON validity |
| Summarization | evidence coverage, unsupported claims, readability |
| QA with retrieval | citation correctness, grounded answer rate |
| Tool routing | correct tool selection and failure recovery |
| Clinical-style drafting | completeness, caveat use, human edit distance |

### Human Evaluation Still Matters

Benchmarks are necessary but insufficient. Domain experts should review representative outputs for:

- biological coherence
- clinical safety language
- correct use of evidence qualifiers
- failure handling when input is incomplete or conflicting

The right question is not “does the model sound smart?” It is “does it help a domain expert work faster without degrading correctness?”

---

## 4.10 Integration With Agentic Oncology Systems

In an agentic system, the LLM is often the planner, formatter, or explanation layer rather than the sole source of truth.

```text
User Request -> LLM Task Classifier -> Retrieval / Tools / Analysis -> Evidence Store -> LLM Synthesis -> Human Review
```

### Productive LLM Roles in Agents

- decompose user goals into tool-appropriate substeps
- translate between natural language and executable queries
- summarize structured outputs into analyst-readable reports
- compare candidate evidence paths and flag ambiguity

### Roles LLMs Should Not Handle Alone

- unsupervised high-impact clinical recommendations
- unsupported factual claims about current trials or evidence tiers
- final adjudication when sources conflict materially
- silent transformation of identifiers or units without validation

This division of labor is what makes LLMs useful in cancer research. They coordinate, explain, and synthesize. Validated tools and curated data should carry the factual weight.

---

## 4.11 Design Principles for Biomedical LLM Systems

Use the following principles when building with LLMs in oncology:

1. ground answers in explicit evidence sources
2. prefer structured outputs over unconstrained prose
3. separate extraction, reasoning, and recommendation stages
4. expose uncertainty rather than hiding it in confident language
5. retain provenance for prompts, tool calls, and generated artifacts
6. keep human review in the loop for high-impact outputs

These principles will recur throughout the rest of the book.

---

## Key Takeaways

- LLMs are valuable in biomedicine because they can connect human scientific language to structured computational workflows.
- Transformer attention enables rich context handling, but biomedical reliability still depends on domain adaptation and grounded system design.
- Hallucinations in oncology are often plausible, subtle, and operationally dangerous rather than obviously absurd.
- Prompting helps most when it constrains task scope, output schema, and uncertainty behavior.
- Tool calling and retrieval are core reliability mechanisms, not optional enhancements.
- The best biomedical LLM systems use models as orchestrators and synthesizers around validated data, tools, and human review.

---

## References

1. Vaswani A, et al. Attention Is All You Need. NeurIPS. 2017.
2. Bommasani R, et al. On the Opportunities and Risks of Foundation Models. 2021.
3. Singhal K, et al. Large Language Models Encode Clinical Knowledge. Nature. 2023.
4. Nori H, et al. Capabilities of GPT-4 on Medical Challenge Problems. 2023.
5. Jin Q, et al. What Disease Does This Patient Have? A Large-Scale Open Domain Question Answering Dataset From Medical Exams. Applied Sciences. 2021.
6. Luo R, et al. BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining. Briefings in Bioinformatics. 2022.
7. Bolton E, et al. PubMedGPT 2.8B. 2024.

---

## Further Reading

- Survey papers on biomedical foundation models and clinical LLM evaluation
- Documentation for PubMed, Europe PMC, CIViC, ClinVar, and cBioPortal APIs
- Model cards and safety evaluations for any biomedical LLM used in production workflows

