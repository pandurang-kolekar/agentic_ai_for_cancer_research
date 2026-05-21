#!/bin/bash

# Script to create theory.md and README.md for all chapters

CHAPTERS=(
  "01|introduction_to_agentic_ai|Introduction to Agentic AI in Cancer Research"
  "02|computational_biology_foundations|Computational Biology Foundations for AI"
  "03|biomedical_data_ecosystems|Biomedical Data Ecosystems"
  "04|large_language_models|Large Language Models for Biomedicine"
  "05|prompt_engineering|Prompt Engineering for Scientific Discovery"
  "06|retrieval_augmented_generation|Retrieval-Augmented Generation in Oncology"
  "07|ai_agents_genomics|AI Agents for Genomics and Variant Interpretation"
  "08|multi_agent_systems|Multi-Agent Systems for Biomedical Research"
  "09|bioinformatics_orchestration|Autonomous Bioinformatics Workflow Orchestration"
  "10|single_cell_spatial_omics|Single-Cell and Spatial Omics Agents"
  "11|knowledge_graphs|Knowledge Graphs and Biomedical Reasoning"
  "12|clinical_translational_oncology|AI for Clinical and Translational Oncology"
  "13|evaluating_biomedical_ai|Evaluating Biomedical AI Systems"
  "14|ethics_governance|Ethics, Governance, and Responsible AI"
  "15|precision_oncology_systems|Building End-to-End Precision Oncology Systems"
  "16|future_directions|Future Directions in Autonomous Scientific Discovery"
  "17|capstone_projects|Capstone Projects and Research Challenges"
)

CHAPTERS_DIR="./chapters"

for CHAPTER_INFO in "${CHAPTERS[@]}"; do
  IFS='|' read -r NUM NAME TITLE <<< "$CHAPTER_INFO"
  
  CHAPTER_DIR="${CHAPTERS_DIR}/chapter_${NUM}_${NAME}"
  
  echo "Creating content for Chapter $NUM: $TITLE"
  
  # Create theory.md
  cat > "${CHAPTER_DIR}/theory.md" << EOF
# Chapter $NUM: $TITLE

## Learning Objectives

By the end of this chapter, you will:

- [ ] Understand the core concepts
- [ ] Learn key methodologies
- [ ] Apply techniques to real-world problems
- [ ] Integrate with other systems

---

## Introduction

*Add introduction content here*

---

## Section 1: Core Concepts

### Subsection 1.1

*Content goes here*

---

## Section 2: Theory and Background

### Subsection 2.1

*Content goes here*

---

## Section 3: Practical Applications

### Subsection 3.1

*Content goes here*

---

## Section 4: Integration with Cancer Research

### Subsection 4.1

*Content goes here*

---

## Key Takeaways

- Point 1
- Point 2
- Point 3

---

## References

*Add references here*

---

## Further Reading

- [Resource 1]
- [Resource 2]
- [Resource 3]

EOF
  
  # Create chapter README.md
  cat > "${CHAPTER_DIR}/README.md" << EOF
# Chapter $NUM: $TITLE

## Overview

This chapter covers the fundamentals of **$TITLE** in the context of agentic AI systems for cancer research.

## Contents

- **[theory.md](theory.md)** - Comprehensive theory and background
- **[notebook.ipynb](notebook.ipynb)** - Hands-on Jupyter notebook with examples

## Learning Objectives

- Understand core concepts
- Learn practical implementations
- Apply to cancer research workflows

## Prerequisites

- Chapter [X] (foundational concepts)
- Python 3.10+
- Jupyter Notebook

## Time to Complete

- Theory: ~30 minutes
- Notebook: ~1-2 hours
- Exercises: ~1-2 hours

## Key Concepts

- Concept 1
- Concept 2
- Concept 3

## How to Use This Chapter

1. **Read theory.md** - Build foundational understanding
2. **Run notebook.ipynb** - Execute code examples
3. **Complete exercises** - Apply concepts to practice problems
4. **Extend examples** - Adapt to your own research

## Data and Resources

- Sample datasets in `datasets/chapter_${NUM}/`
- Reference materials in `resources/`

## Next Steps

After completing this chapter:
- Proceed to Chapter $((NUM + 1))
- Review related chapters as needed
- Apply concepts to your research

## FAQ

**Q: What if I get an error in the notebook?**
A: Check the troubleshooting guide in `resources/troubleshooting.md`

**Q: Can I use different tools/libraries?**
A: Yes! The core concepts apply across different implementations.

## Feedback

Have suggestions or found issues? Open an issue or discussion on GitHub.

---

**Last Updated**: May 2024

EOF
  
  echo "✓ Created for Chapter $NUM"
done

echo ""
echo "✓ All chapter templates created successfully!"

