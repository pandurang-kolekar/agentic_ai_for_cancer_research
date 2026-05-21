# Images and Figures

This folder contains figures, diagrams, and visualizations for the book.

## Structure

```
images/
├── chapter_diagrams/       # Diagrams for each chapter
├── architecture/           # System architecture diagrams
├── workflows/             # Workflow and pipeline diagrams
├── biology/               # Biological illustrations
└── results/               # Example result figures
```

## Usage

All figures are included in the theory.md and notebook.ipynb files using markdown:

```markdown
![Figure Description](../images/chapter_diagrams/figure_name.png)
```

## Adding Figures

To add a figure:
1. Save image to appropriate subdirectory
2. Use descriptive filename (e.g., `rag_pipeline.png`)
3. Reference in markdown with relative path
4. Add alt text for accessibility

## Figure Formats

- Vector: SVG (preferred for diagrams)
- Raster: PNG (preferred for screenshots)
- High-res: Use 300 DPI for print quality

## Attribution

See individual figure captions for source attribution and licenses.

---

**Last Updated**: May 2024

