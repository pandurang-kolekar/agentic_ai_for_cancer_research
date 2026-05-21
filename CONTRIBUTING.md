# Contributing to Agentic AI for Cancer Research

Thank you for your interest in contributing to this book project! We welcome contributions from researchers, educators, and developers.

## How to Contribute

### 1. Reporting Issues

Found a typo, bug, or have a suggestion? Please open an issue:

- Go to [Issues](https://github.com/yourusername/agentic_ai_for_cancer_research/issues)
- Describe the problem clearly with examples
- Include screenshots or code snippets if applicable

### 2. Improving Existing Content

- **Typos/Grammar**: Submit a pull request with corrections
- **Code improvements**: Optimize existing notebooks or examples
- **Clarifications**: Enhance explanations or add missing details

### 3. Adding New Content

- **New chapters**: Discuss in Issues first before starting
- **New datasets**: Follow the format in `datasets/README.md`
- **New examples**: Add to relevant chapter notebooks

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your code/notebooks thoroughly
5. Commit with clear messages: `git commit -m "Clear description of changes"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Open a Pull Request with:
   - Clear title and description
   - Reference to related issues
   - List of changes made

## Content Guidelines

### Theory Content (theory.md)

- Use clear, scientific language
- Include references and citations
- Add section headers with proper hierarchy
- Keep paragraphs focused (2-4 sentences)
- Use LaTeX for equations
- Include figures and diagrams

### Notebooks

- Follow PEP 8 style guide
- Add descriptive markdown cells
- Include comments for complex code
- Add docstrings to functions
- Test all code before submitting
- Provide example outputs
- Keep notebooks under 20 MB

### Code Quality

```python
# Good: Clear, documented code
def calculate_similarity(seq1: str, seq2: str) -> float:
    """
    Calculate sequence similarity using Jaccard index.
    
    Args:
        seq1: First DNA sequence
        seq2: Second DNA sequence
        
    Returns:
        float: Similarity score (0-1)
    """
    kmers1 = set(seq1[i:i+3] for i in range(len(seq1)-2))
    kmers2 = set(seq2[i:i+3] for i in range(len(seq2)-2))
    return len(kmers1 & kmers2) / len(kmers1 | kmers2)
```

### Markdown Formatting

Use consistent formatting:

```markdown
# Chapter Title
## Section
### Subsection

**Bold for emphasis**
*Italics for terminology*
`code` for inline code

- Bullet lists
  - Nested items
  
1. Numbered lists
2. With items

> Blockquotes for important notes

[Link text](url)
```

## Style Guide

### Scientific Writing

- Use active voice when possible
- Define acronyms on first use
- Be precise with technical terms
- Provide context for domain-specific concepts
- Include citations for facts and methods

### Code Comments

```python
# Explain the WHY, not the WHAT
# BAD: x = x + 1  # increment x
# GOOD: x += 1  # Move to next sample index
```

### Naming Conventions

- Python: `snake_case` for functions/variables, `PascalCase` for classes
- Notebooks: Descriptive names, e.g., `chapter_01_biomedical_assistant.ipynb`
- Files: lowercase with underscores, e.g., `dna_sequence_analysis.py`

## Testing

Before submitting:

1. Run notebooks from start to finish
2. Check all links work
3. Verify code examples run without errors
4. Validate figures display correctly
5. Test on Python 3.10+

## Commit Message Guidelines

```
Type: Brief description (50 chars max)

Detailed explanation of changes (72 chars per line).
Reference issues: Fixes #123

Examples:
- feat: Add ChIP-seq analysis notebook
- fix: Correct sequence alignment algorithm
- docs: Clarify RAG pipeline section
- refactor: Optimize performance in chapter 8
```

Types:
- `feat`: New feature or content
- `fix`: Bug fix or correction
- `docs`: Documentation update
- `refactor`: Code reorganization
- `test`: Test additions/updates
- `chore`: Maintenance tasks

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Contributors should:

- Be respectful and professional
- Provide constructive feedback
- Acknowledge differing opinions
- Focus on the content, not the person
- Help others learn and grow

## Questions?

- Email: [your-email@example.com]
- Open a Discussion: [GitHub Discussions](https://github.com/yourusername/agentic_ai_for_cancer_research/discussions)
- Check existing issues and PRs first

## Recognition

Contributors will be acknowledged in:
- The book's contributors section
- GitHub contributors page
- Individual chapter credits

Thank you for making this project better! 🙏

