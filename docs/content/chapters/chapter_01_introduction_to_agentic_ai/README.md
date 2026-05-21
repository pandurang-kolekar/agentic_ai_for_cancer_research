# Chapter 01: Introduction to Agentic AI in Cancer Research

## Overview

This chapter introduces agentic AI as a practical computational paradigm for oncology and translational research. It explains how agents differ from traditional machine learning systems, why cancer research benefits from planning and tool-using AI systems, and where human oversight must remain central.

## Contents

- **[theory.md](theory.md)** - Comprehensive theory and background
- **[notebook.ipynb](notebook.ipynb)** - Hands-on Jupyter notebook with examples

## Section Map

- **1.1 The Evolution of AI Systems** - From rule-based systems to agentic AI
- **1.2 Defining Agentic AI** - What makes an AI system agentic in practice
- **1.3 Why Cancer Research Needs Agentic AI** - Data scale, literature growth, and translational complexity
- **1.4 Core Components of AI Agents** - Planning, memory, retrieval, tool use, reflection, and oversight
- **1.5 Agentic Systems vs Traditional Pipelines** - When adaptive orchestration helps and when fixed workflows remain better
- **1.6 Representative Biomedical Use Cases** - Literature mining, variant interpretation, single-cell workflows, and trial matching
- **1.7 Limitations, Risks, and Governance** - Safety, hallucinations, evidence quality, and accountability
- **1.8 Human-in-the-Loop Design Principles** - How to keep biomedical agents useful and reviewable

## Learning Objectives

- Define agentic AI and distinguish it from conventional predictive systems
- Explain the core components of biomedical agents
- Identify high-value oncology use cases and major risks
- Build intuition for evidence-grounded, human-supervised agent workflows

## Prerequisites

- Basic familiarity with Python and Jupyter notebooks
- General understanding of cancer research workflows or biomedical data analysis
- Python 3.10+
- Jupyter Notebook

## Time to Complete

- Theory: ~35-45 minutes
- Notebook: ~45-60 minutes
- Exercises: ~30-45 minutes

## Key Concepts

- Agentic AI vs traditional pipelines
- Planning, memory, retrieval, tool use, and reflection
- Human-in-the-loop biomedical workflows
- Evidence grounding and governance in oncology AI
- Research workflow decomposition for oncology questions

## How to Use This Chapter

1. **Read theory.md** - Build the conceptual foundation for agentic systems in cancer research
2. **Run notebook.ipynb** - Explore visual summaries, workflow scoring, and evidence-grounding examples
3. **Complete exercises** - Practice converting research tasks into agent plans
4. **Extend examples** - Adapt the workflow mapping to your own domain questions

## Data and Resources

- No external dataset is required for the core notebook walkthrough
- Reference materials are listed in theory.md and the repository resources directory
- The notebook uses synthetic examples so you can focus on concepts before connecting real biomedical APIs or datasets

## Suggested Reading Path

If you are new to the topic, read Sections 1.1 to 1.4 first to understand the architectural ideas. Then use Sections 1.5 to 1.8 to decide where agentic systems are helpful, where they are risky, and how human review should constrain them. After that, run the notebook to translate those ideas into a simple research workflow design exercise.

## Next Steps

After completing this chapter:
- Proceed to Chapter 2 for the biological foundations needed to ground later agent workflows
- Revisit this chapter when designing RAG, multi-agent, or workflow orchestration systems later in the book
- Apply the planning and evidence-grounding ideas to your own research questions

## References Highlight

- TCGA Pan-Cancer analysis for multi-omics scale in oncology
- FAIR principles for reproducible computational research
- Retrieval-augmented generation and LLM agent surveys for grounding and orchestration

## FAQ

**Q: What if I get an error in the notebook?**
A: Check the setup instructions in /resources/setup_guide.md and confirm the environment includes the plotting libraries listed in /resources/requirements.txt.

**Q: Can I use different tools/libraries?**
A: Yes! The core concepts apply across different implementations.

**Q: Does this chapter build a full autonomous research agent?**
A: No. This chapter focuses on the concepts and workflow design patterns that make later agent implementations interpretable and safer.

## Feedback

Have suggestions or found issues? Open an issue or discussion on GitHub.

---

**Last Updated**: May 2026

