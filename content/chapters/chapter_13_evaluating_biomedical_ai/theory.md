# Chapter 13: Evaluating Biomedical AI Systems

## Learning Objectives

By the end of this chapter, you will:

- define evaluation plans that match biomedical use-case risk and deployment stage
- measure retrieval, reasoning, and generation quality with domain-relevant metrics
- test robustness across cohorts, institutions, and pediatric or rare-disease contexts
- evaluate calibration, uncertainty behavior, and abstention quality
- design post-deployment monitoring and rollback criteria for safe iteration

---

## Introduction

Evaluation is the difference between a promising demo and a trustworthy biomedical system. In oncology, errors can propagate into experimental priorities, trial screening, and case discussions. That makes evaluation a scientific and operational discipline, not a final checkbox.

Many AI projects over-index on one metric, such as benchmark accuracy, while under-evaluating failure behavior, subgroup stability, and real workflow utility. Biomedical AI needs broader evidence: technical correctness, clinical plausibility, uncertainty quality, reproducibility, and impact on user decisions.

This chapter provides a practical framework for evaluating biomedical AI systems end-to-end, from offline benchmarks to post-deployment monitoring.

---

## 13.1 Evaluation Scope and Risk Tiering

Evaluation depth should scale with potential impact.

### Suggested Risk Tiers

- low risk: literature triage and internal drafting support
- medium risk: research decision support and prioritization tasks
- high risk: clinical-facing recommendations or patient-proximal outputs

### Consequences for Evaluation

- higher risk requires stricter validation, stronger abstention behavior, and human review gates
- lower risk can prioritize productivity metrics with lighter governance overhead

Risk-tiered evaluation prevents under-testing of high-impact workflows.

---

## 13.2 Offline Technical Evaluation

Offline testing remains foundational.

### Core Technical Metrics

- extraction tasks: precision, recall, F1, schema validity
- retrieval tasks: recall@k, precision@k, MRR
- generation tasks: grounded claim rate, unsupported claim rate, citation fidelity
- routing tasks: tool-selection accuracy and failure recovery rate

### Dataset Design Principles

- include edge cases (rare variants, pediatric cohorts, conflicting evidence)
- separate train/validation/test with no leakage
- preserve temporal splits where evidence recency matters

Technical metrics are necessary but not sufficient for biomedical trust.

---

## 13.3 Clinical and Translational Validity

Model correctness must be judged in domain context.

### Domain Validity Questions

- are claims consistent with source evidence and context?
- are confidence statements calibrated to evidence quality?
- are critical caveats included when evidence is weak or conflicting?
- are adult and pediatric contexts kept distinct?

### Human Review Protocols

- blinded expert review on representative samples
- disagreement adjudication with explicit error categories
- track changes needed before analyst or clinician acceptance

Human review outcomes should be treated as first-class evaluation signals.

---

## 13.4 Robustness and Generalization Testing

Biomedical data shifts across time, site, and population.

### Robustness Axes

- institution/site shift
- assay/platform shift
- demographic and ancestry subgroup variation
- temporal evidence drift

### Stress Tests

- perturb prompts while preserving intent
- inject incomplete metadata scenarios
- test adversarial ambiguity in gene or disease terms
- evaluate recovery under tool/API failure

Robust systems degrade gracefully instead of failing silently.

---

## 13.5 Calibration, Uncertainty, and Abstention

In high-stakes domains, confidence quality can matter more than raw accuracy.

### What to Measure

- calibration error between predicted confidence and correctness
- abstention precision (how often abstentions prevent bad outputs)
- overconfidence rate in low-support cases

### Practical Policy

- enforce low-confidence escalation rather than forced completion
- require structured uncertainty fields in outputs
- audit all high-confidence outputs for citation support

Safe systems know when not to answer.

---

## 13.6 Workflow and User-Centered Evaluation

A system that is accurate but unusable will not improve outcomes.

### Workflow Metrics

- time-to-useful-answer
- human edit distance to accepted output
- reviewer override rate
- escalation appropriateness rate

### User Studies

- evaluate with target users (bioinformaticians, researchers, clinicians)
- capture cognitive load and trust calibration
- test realistic multi-step workflows, not isolated prompts

Operational fit is part of scientific validity.

---

## 13.7 Safety Evaluation and Incident Taxonomy

Define explicit failure classes before deployment.

### Example Failure Taxonomy

- unsupported biomedical claim
- incorrect context transfer (tumor type or age group)
- missing critical caveat
- citation mismatch or fabrication
- tool-routing failure causing incomplete evidence

### Safety Program Elements

- red-team evaluation suites
- near-miss logging and root-cause analysis
- remediation playbooks with ownership and timelines

Continuous safety learning is required for sustained reliability.

---

## 13.8 Reproducibility and Evaluation Governance

Evaluation must be repeatable and auditable.

### Reproducibility Controls

- versioned datasets and benchmark snapshots
- prompt, model, and tool version tracking
- fixed evaluation scripts with change control
- reproducible reports and run manifests

### Governance Controls

- approval gates for metric target changes
- documented acceptance criteria by risk tier
- periodic review board for metric drift and blind spots

Unversioned evaluation leads to unreliable progress claims.

---

## 13.9 Post-Deployment Monitoring

Performance can drift after launch.

### Monitoring Signals

- subgroup error-rate changes
- citation fidelity degradation
- increases in abstention or override rates
- latency or tool failure spikes

### Response Strategy

1. detect and triage anomaly
2. quantify impact and affected scope
3. mitigate (rollback, threshold update, hotfix)
4. run post-incident review and update safeguards

Monitoring closes the loop between development and real-world performance.

---

## Key Takeaways

- Biomedical AI evaluation must be risk-tiered and end-to-end.
- Offline metrics should be combined with domain review, robustness tests, and workflow impact.
- Calibration and abstention quality are core safety properties.
- Reproducibility requires strict versioning of datasets, prompts, models, and tools.
- Post-deployment monitoring is mandatory due to drift and workflow change.
- Strong evaluation culture is foundational to responsible oncology AI.

---

## References

1. Wiens J, et al. Do No Harm: A Roadmap for Responsible Machine Learning for Health Care. Nature Medicine. 2019.
2. Kelly CJ, et al. Key Challenges for Delivering Clinical Impact With Artificial Intelligence. BMC Medicine. 2019.
3. Topol EJ. High-Performance Medicine: The Convergence of Human and Artificial Intelligence. Nature Medicine. 2019.
4. Collins GS, et al. TRIPOD-AI and PROBAST-AI initiative papers. 2021.
5. Gao Y, et al. Retrieval-Augmented Generation for Large Language Models: A Survey. 2023.

---

## Further Reading

- Guidance documents on clinical AI validation and monitoring
- Benchmark design papers for biomedical NLP and retrieval systems
- Human factors literature for decision-support tool evaluation

