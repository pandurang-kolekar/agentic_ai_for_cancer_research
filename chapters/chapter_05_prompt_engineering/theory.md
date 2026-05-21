# Chapter 05: Prompt Engineering for Scientific Discovery

## Learning Objectives

By the end of this chapter, you will:

- design biomedical prompts that separate extraction, reasoning, and recommendation tasks
- create structured prompt templates for oncology, genomics, and translational workflows
- apply context controls that reduce unsupported or overconfident model claims
- build evaluation rubrics for prompt quality, grounding, and reproducibility
- connect prompt design to downstream tool calls, retrieval, and human-review checkpoints

---

## Introduction

Prompt engineering is the practice of converting a research intent into precise model instructions that produce useful and auditable outputs. In biomedical settings, this is not only about style. It is about scientific control. A well-designed prompt can guide an LLM toward evidence-linked extraction, explicit uncertainty handling, and machine-readable outputs. A weak prompt can encourage plausible but unsupported conclusions.

In cancer research, prompt quality has direct operational consequences. Prompt instructions influence what claims are made, which evidence is surfaced, and whether downstream analysts can verify the output quickly. Because oncology evidence is context-sensitive and rapidly evolving, prompt design should be treated as part of system design rather than an ad hoc last step.

This chapter provides a practical framework for building prompt workflows that are reproducible, domain-aware, and compatible with later chapters on retrieval and multi-agent orchestration.

---

## 5.1 Why Prompt Engineering Matters in Biomedicine

LLMs are sensitive to framing. The same model can behave like an extractor, a speculative advisor, or a conservative assistant depending on prompt instructions.

### Biomedical Consequences of Prompt Framing

- determines whether output distinguishes evidence from inference
- controls how uncertainty and conflicts are represented
- affects whether rare/pediatric contexts are acknowledged or ignored
- determines whether outputs are parseable for downstream tools

### Common Failure From Weak Prompts

Generic instructions such as "interpret this mutation" combine multiple tasks and hide assumptions. The model may blur evidence extraction, mechanism interpretation, and clinical implications into one fluent paragraph that is difficult to validate.

Prompt engineering is valuable because it makes task boundaries explicit.

---

## 5.2 Prompt Anatomy for Scientific Work

A robust biomedical prompt should encode role, task, context, output constraints, and safety rules.

### Recommended Prompt Components

1. role and scope
2. task objective
3. domain context and constraints
4. output schema
5. evidence and uncertainty rules
6. escalation or abstention behavior

### Template Example

```text
Role:
You are an oncology evidence extraction assistant.

Task:
Extract only claims directly supported by the provided source text.

Context:
Tumor type: pediatric high-grade glioma
Question: summarize evidence for H3F3A K27M

Output format:
Return JSON with keys:
- gene
- alteration
- tumor_type
- evidence_statement
- confidence
- unsupported_claims_detected

Rules:
- Do not add external facts.
- If support is weak or absent, set unsupported_claims_detected=true.
- If key context is missing, return insufficient_evidence.
```

This structure reduces ambiguity and makes evaluation easier.

---

## 5.3 Prompt Patterns for Oncology Tasks

Different biomedical tasks require different prompt patterns.

### Pattern A: Extraction Prompt

Use when you need factual fields from a source.

- objective: maximize precision and schema validity
- output: structured JSON
- risk focus: fabricated claims or omitted qualifiers

### Pattern B: Evidence Synthesis Prompt

Use when multiple passages or records must be merged.

- objective: summarize while preserving provenance
- output: concise synthesis with explicit citation slots
- risk focus: collapsing conflicting evidence into false consensus

### Pattern C: Routing Prompt

Use when deciding next tool call or workflow step.

- objective: map intent to a limited tool set
- output: selected tool plus rationale
- risk focus: incorrect tool choice and hidden assumptions

### Pattern D: Critique Prompt

Use as a second-pass checker over draft output.

- objective: find unsupported, overconfident, or missing claims
- output: issue list with severity labels
- risk focus: false reassurance from single-pass generation

---

## 5.4 Context Engineering: What to Include and What to Exclude

Prompt quality depends on context quality. More context is not always better.

### Include

- disease and subtype context
- assay modality and data source
- temporal scope (publication date window or release version)
- intended audience (bioinformatician, clinician, multidisciplinary team)
- acceptance criteria for outputs

### Exclude

- irrelevant narrative that distracts from task objective
- conflicting instructions in the same prompt
- unverifiable requests for definitive conclusions

### Practical Rule

Include only context that changes the decision boundary. If a field does not change what "correct" means, it likely belongs outside the prompt.

---

## 5.5 Reducing Hallucinations With Prompt Constraints

Prompt constraints cannot guarantee truth, but they reduce uncontrolled generation.

### High-Leverage Constraints

- evidence-only mode (no external facts)
- fixed schemas and controlled vocabularies
- confidence labels with explicit meanings
- mandatory "insufficient_evidence" behavior
- required citation placeholders or IDs

### Confidence Labeling Example

Define confidence in prompt instructions:

- high: direct evidence in provided source text
- medium: partial support with unresolved context
- low: weak support or missing critical context

When confidence semantics are explicit, outputs become easier to compare across runs.

---

## 5.6 Few-Shot and Demonstration Design

Few-shot prompting adds examples to steer behavior. In biomedicine, example quality matters more than example count.

### Good Demonstration Characteristics

- domain-relevant examples with realistic terminology
- explicit positive and negative examples
- edge cases (rare variants, pediatric subtypes, conflicting sources)
- strict adherence to the target output schema

### Frequent Few-Shot Pitfalls

- examples that leak unsupported clinical claims
- inconsistent formatting between examples
- too many examples that crowd out task instructions
- examples from one tumor context reused uncritically in another

Treat few-shot sets as versioned artifacts with review history.

---

## 5.7 Prompt Evaluation and Versioning

Prompt engineering should be empirical. Evaluate prompts with a benchmark set and track revisions.

### Minimum Evaluation Metrics

- schema validity rate
- unsupported claim rate
- omission rate for required fields
- consistency across repeated runs
- human edit distance for final analyst-ready output

### Prompt Versioning Practices

- assign stable IDs (for example, `prompt_onco_extract_v3`)
- store change logs and rationale
- keep benchmark snapshots tied to prompt versions
- record model version and temperature settings

Without versioning, improvements are anecdotal and regressions are hard to detect.

---

## 5.8 Prompt Chaining for Complex Biomedical Tasks

Complex tasks should be decomposed into chained prompts rather than solved in one generation step.

### Example Chain: Variant Evidence Pipeline

1. extraction prompt: parse gene, alteration, tumor context
2. retrieval prompt: formulate source-specific query terms
3. synthesis prompt: merge retrieved evidence with caveats
4. critique prompt: flag unsupported or overconfident statements
5. final formatter prompt: produce analyst-facing report template

This staged design improves transparency and error localization.

---

## 5.9 Integration With Tool Calling and Agents

Prompt design should align with available tools and policy constraints.

```text
User Intent -> Prompt Classifier -> Tool Selection -> Retrieved Evidence -> Structured Prompt -> Output Validator -> Human Review
```

### Agent-Aware Prompt Rules

- prompts should request exactly the fields required by the next tool
- outputs should be machine-parseable without fragile post-processing
- failure states should trigger deterministic retries or escalation
- tool provenance should be included in the final synthesis prompt

Prompt engineering becomes more valuable when it is treated as interface design between model reasoning and system tooling.

---

## 5.10 Governance and Safety for Biomedical Prompting

Biomedical prompts should embed governance norms, not just technical constraints.

### Recommended Safety Clauses

- "Do not provide treatment recommendations without explicit evidence fields"
- "If trial eligibility is uncertain, output requires_human_review"
- "Never fabricate citation metadata"
- "Do not infer pediatric applicability from adult-only evidence"

### Operational Controls

- role-based access to prompt templates in production
- approval workflow for high-impact prompt updates
- red-team tests for known failure categories
- audit logs linking outputs to prompt/model/tool versions

Safety is not a model feature alone. It is a prompt-plus-process property.

---

## Key Takeaways

- Prompt engineering in oncology is a control layer for scientific validity, not merely wording optimization.
- Strong prompts make task boundaries explicit and separate extraction from interpretation.
- Context design should be selective and clinically meaningful, not maximally verbose.
- Structured outputs, confidence rules, and abstention behavior reduce unsupported claims.
- Prompt evaluation and versioning are required for reproducible improvements.
- Prompt patterns should be designed alongside retrieval, tool calling, and human-review workflows.

---

## References

1. Reynolds L, McDonell K. Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm. 2021.
2. White J, et al. A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT. 2023.
3. Singhal K, et al. Large Language Models Encode Clinical Knowledge. Nature. 2023.
4. Nori H, et al. Capabilities of GPT-4 on Medical Challenge Problems. 2023.
5. Meskovic M, et al. Large Language Models in Biomedical Research: Opportunities and Risks. 2024.

---

## Further Reading

- Prompt design pattern libraries for structured AI workflows
- Biomedical LLM evaluation studies focused on hallucination and calibration
- Model cards and safety documentation for production LLM systems

