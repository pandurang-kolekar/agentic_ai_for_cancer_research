# Chapter 17: Capstone Projects and Research Challenges

## Learning Objectives

By the end of this chapter, you will:

- formulate capstone projects with clear scientific questions and measurable success criteria
- design end-to-end project architectures that integrate data, retrieval, agents, and governance
- plan evaluation strategies spanning technical, translational, and operational outcomes
- identify common project risks and mitigation approaches
- build dissemination and reproducibility plans for publishable and reusable outputs

---

## Introduction

Capstone projects are where concepts become systems. After learning data ecosystem design, LLM grounding, retrieval, orchestration, knowledge graphs, and governance, the next step is to build integrated solutions for real biomedical problems. Effective capstones are scoped to deliver clear value while demonstrating scientific rigor and responsible AI practices.

This chapter provides practical guidance for selecting project themes, defining architecture, planning milestones, and evaluating outcomes. It is designed to help teams move from prototype ideas to defensible, reproducible research artifacts.

---

## 17.1 Choosing a High-Value Capstone Problem

Project selection should balance novelty, feasibility, and impact.

### Selection Criteria

- clinical or translational relevance
- data availability and governance feasibility
- clear evaluation pathway
- opportunity for methodological contribution
- manageable scope within timeline constraints

### Example Problem Types

- variant interpretation copilots with evidence traceability
- trial pre-screening assistants with uncertainty-aware outputs
- multi-agent literature-to-report synthesis systems
- microenvironment-aware target prioritization tools

Strong projects solve concrete problems with measurable outcomes.

---

## 17.2 Capstone Architecture Blueprint

Most capstones should follow a modular architecture.

```text
Data Ingestion -> Harmonization -> Knowledge Layer -> Retrieval/Tools -> Agent Workflow -> Evaluation Dashboard -> Human Review
```

### Mandatory Components

- reproducible data pipeline
- structured output schema
- citation and provenance tracking
- evaluation harness with benchmark cases
- governance controls and escalation paths

Modularity simplifies testing and future extension.

---

## 17.3 Recommended Capstone Tracks

### Track A: Biomedical RAG System

- focus: grounded QA and evidence synthesis
- contribution options: retrieval optimization, citation fidelity auditing

### Track B: Genomics Agent Pipeline

- focus: annotation, evidence retrieval, and structured report generation
- contribution options: uncertainty calibration, conflict resolution logic

### Track C: Multi-Agent Research Assistant

- focus: planner + specialist + critic collaboration
- contribution options: communication protocols and failure recovery

### Track D: Translational Workflow Support

- focus: trial matching and tumor-board preparation support
- contribution options: human factors and workflow integration metrics

Choose one primary track and one secondary stretch goal.

---

## 17.4 Milestone Planning and Execution

Use milestone-based delivery to manage scope.

### Example Milestones

1. problem definition and success metrics
2. baseline pipeline and initial benchmark
3. agent/retrieval integration
4. evaluation and robustness testing
5. governance hardening and final demonstration

### Execution Practices

- weekly review of risk register
- versioned experiment tracking
- issue triage by severity and impact
- explicit go/no-go criteria per milestone

Predictable progress is more valuable than unstable feature breadth.

---

## 17.5 Evaluation Plan for Capstones

Evaluation should be defined before implementation completes.

### Minimum Evaluation Stack

- technical metrics: correctness, retrieval quality, schema validity
- domain metrics: evidence relevance, unsupported-claim rate
- workflow metrics: time saved, edit distance, user acceptance
- safety metrics: escalation appropriateness and failure visibility

### Experimental Design Tips

- include baseline systems for comparison
- test edge cases and subgroup scenarios
- separate development and final holdout sets

Capstone credibility depends on rigorous and transparent evaluation.

---

## 17.6 Reproducibility and Documentation Requirements

Projects should be reproducible by other teams.

### Required Artifacts

- architecture diagram and system description
- setup instructions and dependency manifests
- benchmark dataset description and versioning
- prompt/model/tool version logs
- evaluation scripts and result summaries

### Documentation Standard

- capture assumptions and known limitations
- list unresolved issues and future work
- provide clear run instructions for core demos

Reproducibility is a deliverable, not an optional add-on.

---

## 17.7 Common Failure Modes in Capstone Projects

### Frequent Pitfalls

- overly broad scope with weak evaluation depth
- strong demos without reproducible setup
- missing governance and safety controls
- reliance on proprietary APIs without fallback plan
- unclear ownership of integration and monitoring tasks

### Mitigation Approaches

- enforce strict scope boundaries
- prioritize robust core pipeline over optional features
- schedule dedicated validation and documentation sprints

Most capstone failures are project-management failures, not model failures.

---

## 17.8 Publishing and Open Science Strategy

Capstones should aim for reusable scientific value.

### Dissemination Options

- technical report or preprint
- open-source reference implementation
- reproducible notebook and benchmark bundle
- demo videos and workshop submissions

### Open Science Practices

- clear licensing
- de-identified or synthetic demo datasets where needed
- transparent limitations and bias statements

Good dissemination multiplies capstone impact.

---

## 17.9 Team Roles and Collaboration Model

Define explicit roles to reduce coordination overhead.

### Suggested Roles

- project lead and systems integrator
- data and retrieval engineer
- model and agent developer
- evaluation and safety lead
- documentation and dissemination lead

### Collaboration Norms

- shared definition of done
- structured code review and design review
- incident and blocker escalation protocol

Role clarity improves delivery and quality.

---

## 17.10 Capstone Completion Checklist

- problem statement and use-case scope finalized
- baseline and improved system compared quantitatively
- safety and governance checks documented
- reproducibility artifacts validated on clean environment
- final presentation includes limitations and next steps

Capstones should conclude with honest evidence of both achievements and gaps.

---

## Key Takeaways

- Strong capstones combine technical depth with translational relevance.
- Modular architecture and milestone planning reduce integration risk.
- Evaluation rigor is essential for project credibility.
- Reproducibility and documentation are core project outputs.
- Safety, governance, and responsible-AI controls should be embedded from the start.
- Clear team roles and disciplined execution drive successful delivery.

---

## References

1. Sandve GK, et al. Ten Simple Rules for Reproducible Computational Research. PLoS Computational Biology. 2013.
2. Wilkinson MD, et al. The FAIR Guiding Principles for Scientific Data Management and Stewardship. Scientific Data. 2016.
3. Peng RD. Reproducible Research in Computational Science. Science. 2011.
4. Wiens J, et al. Do No Harm: A Roadmap for Responsible Machine Learning for Health Care. Nature Medicine. 2019.
5. Kelly CJ, et al. Key Challenges for Delivering Clinical Impact With Artificial Intelligence. BMC Medicine. 2019.

---

## Further Reading

- Capstone design and project management resources for computational research
- FAIR data and reproducibility checklists
- Biomedical AI reporting guidelines for transparent publication

