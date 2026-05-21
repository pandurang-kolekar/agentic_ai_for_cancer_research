#!/usr/bin/env python3
"""
Script to create Jupyter notebook templates for all chapters
"""

import json
import os

CHAPTERS = [
    (1, "Introduction to Agentic AI in Cancer Research"),
    (2, "Computational Biology Foundations for AI"),
    (3, "Biomedical Data Ecosystems"),
    (4, "Large Language Models for Biomedicine"),
    (5, "Prompt Engineering for Scientific Discovery"),
    (6, "Retrieval-Augmented Generation in Oncology"),
    (7, "AI Agents for Genomics and Variant Interpretation"),
    (8, "Multi-Agent Systems for Biomedical Research"),
    (9, "Autonomous Bioinformatics Workflow Orchestration"),
    (10, "Single-Cell and Spatial Omics Agents"),
    (11, "Knowledge Graphs and Biomedical Reasoning"),
    (12, "AI for Clinical and Translational Oncology"),
    (13, "Evaluating Biomedical AI Systems"),
    (14, "Ethics, Governance, and Responsible AI"),
    (15, "Building End-to-End Precision Oncology Systems"),
    (16, "Future Directions in Autonomous Scientific Discovery"),
    (17, "Capstone Projects and Research Challenges"),
]

def create_notebook(chapter_num, chapter_title):
    """Create a Jupyter notebook template for a chapter"""
    
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Chapter {chapter_num}: {chapter_title}\n",
                    "\n",
                    "## Hands-On Jupyter Notebook\n",
                    "\n",
                    f"This notebook provides interactive exercises and code examples for Chapter {chapter_num}.\n",
                    "\n",
                    "**Time to Complete**: 1-2 hours\n",
                    "\n",
                    "---"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Section 1: Setup and Imports\n",
                    "\n",
                    "First, let's import the necessary libraries and set up our environment."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Standard library imports\n",
                    "import os\n",
                    "from typing import List, Dict, Tuple\n",
                    "import warnings\n",
                    "warnings.filterwarnings('ignore')\n",
                    "\n",
                    "# Data processing\n",
                    "import numpy as np\n",
                    "import pandas as pd\n",
                    "\n",
                    "# Visualization\n",
                    "import matplotlib.pyplot as plt\n",
                    "import seaborn as sns\n",
                    "sns.set_style('whitegrid')\n",
                    "\n",
                    "# Configuration\n",
                    "plt.rcParams['figure.figsize'] = (12, 6)\n",
                    "np.random.seed(42)\n",
                    "\n",
                    "print('✓ Environment configured successfully!')"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Section 2: Load Data and Explore\n",
                    "\n",
                    "In this section, we'll load sample data and perform initial exploration."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example: Load sample data\n",
                    "# Replace this with your actual data loading code\n",
                    "\n",
                    "# Create sample DataFrame\n",
                    "sample_data = pd.DataFrame({\n",
                    "    'sample_id': [f'sample_{i}' for i in range(100)],\n",
                    "    'value1': np.random.randn(100),\n",
                    "    'value2': np.random.randn(100),\n",
                    "    'category': np.random.choice(['A', 'B', 'C'], 100)\n",
                    "})\n",
                    "\n",
                    "print('Dataset shape:', sample_data.shape)\n",
                    "print('\\nFirst few rows:')\n",
                    "sample_data.head()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Section 3: Main Analysis\n",
                    "\n",
                    "Implement the core analysis or method from this chapter."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Add your main analysis code here\n",
                    "# This is where you implement the chapter's key concepts\n",
                    "\n",
                    "print('Analysis placeholder for Chapter', {chapter_num})"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Section 4: Visualization\n",
                    "\n",
                    "Create visualizations to present findings."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example visualization\n",
                    "fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n",
                    "\n",
                    "# Plot 1: Distribution\n",
                    "axes[0].hist(sample_data['value1'], bins=20, alpha=0.7, edgecolor='black')\n",
                    "axes[0].set_xlabel('Value1')\n",
                    "axes[0].set_ylabel('Frequency')\n",
                    "axes[0].set_title('Distribution of Value1')\n",
                    "\n",
                    "# Plot 2: Scatter plot by category\n",
                    "for cat in sample_data['category'].unique():\n",
                    "    mask = sample_data['category'] == cat\n",
                    "    axes[1].scatter(sample_data[mask]['value1'], \n",
                    "                   sample_data[mask]['value2'],\n",
                    "                   label=f'Category {cat}',\n",
                    "                   alpha=0.6)\n",
                    "\n",
                    "axes[1].set_xlabel('Value1')\n",
                    "axes[1].set_ylabel('Value2')\n",
                    "axes[1].set_title('Value1 vs Value2 by Category')\n",
                    "axes[1].legend()\n",
                    "\n",
                    "plt.tight_layout()\n",
                    "plt.show()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Section 5: Exercises\n",
                    "\n",
                    "### Exercise 1: [Title]\n",
                    "\n",
                    "*Description: Complete this exercise to practice the concepts from this chapter*"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Exercise 1: [Instructions]\n",
                    "# TODO: Implement your solution here\n",
                    "\n",
                    "# Your code goes here\n",
                    "pass"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "### Exercise 2: [Title]\n",
                    "\n",
                    "*Description: Challenge yourself with this advanced exercise*"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Exercise 2: [Instructions]\n",
                    "# TODO: Implement your solution here\n",
                    "\n",
                    "# Your code goes here\n",
                    "pass"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Section 6: Key Takeaways\n",
                    "\n",
                    "- **Key Point 1**: Main concept from this chapter\n",
                    "- **Key Point 2**: Application to cancer research\n",
                    "- **Key Point 3**: Integration with other systems\n",
                    "\n",
                    "---\n",
                    "\n",
                    "## Next Steps\n",
                    "\n",
                    "1. ✅ Complete all exercises\n",
                    "2. 📖 Read Chapter " + str(chapter_num + 1) + " (next chapter)\n",
                    "3. 🔗 Review related chapters as needed\n",
                    "4. 🧪 Extend examples to your own research\n",
                    "\n",
                    "---\n",
                    "\n",
                    "**Last Updated**: May 2024"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (agentic-ai-cancer)",
                "language": "python",
                "name": "agentic-ai-cancer"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    
    return notebook

def main():
    """Create notebooks for all chapters"""
    base_path = "chapters"
    
    for chapter_num, chapter_title in CHAPTERS:
        # Build chapter directory name
        chapter_folder = f"chapter_{chapter_num:02d}"
        for item in os.listdir(base_path):
            if item.startswith(chapter_folder):
                chapter_path = os.path.join(base_path, item)
                break
        
        if not os.path.exists(chapter_path):
            print(f"Warning: Could not find directory for Chapter {chapter_num}")
            continue
        
        # Create notebook
        notebook = create_notebook(chapter_num, chapter_title)
        notebook_file = os.path.join(chapter_path, "notebook.ipynb")
        
        # Write notebook
        with open(notebook_file, 'w') as f:
            json.dump(notebook, f, indent=2)
        
        print(f"✓ Created notebook for Chapter {chapter_num}: {chapter_title}")
    
    print("\n✓ All notebooks created successfully!")

if __name__ == "__main__":
    main()

