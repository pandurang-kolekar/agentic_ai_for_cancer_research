# Appendix F: Notebook Setup Guide

## Overview

This guide provides setup instructions specific to Jupyter notebooks in this book.

## Contents

1. Kernel Selection
2. Virtual Environment Integration
3. Working with Notebooks
4. Package Management in Notebooks
5. Troubleshooting

## 1. Kernel Selection

### Create Conda Kernel

```bash
conda activate agentic-ai-cancer
python -m ipykernel install --user --name agentic-ai-cancer --display-name "Python (Agentic AI)"
```

### Create Virtual Environment Kernel

```bash
source venv/bin/activate
python -m ipykernel install --user --name agentic-ai --display-name "Python (Agentic AI venv)"
```

## 2. Virtual Environment Integration

### Check Available Kernels

```bash
jupyter kernelspec list
```

### Remove Kernel

```bash
jupyter kernelspec uninstall agentic-ai-cancer
```

## 3. Working with Notebooks

### Launch Jupyter Lab

```bash
jupyter lab
```

### Launch Specific Notebook

```bash
jupyter lab chapters/chapter_01_introduction_to_agentic_ai/notebook.ipynb
```

### Convert Notebook to Script

```bash
jupyter nbconvert --to script notebook.ipynb
```

### Execute Notebook Programmatically

```bash
jupyter nbconvert --to notebook --execute input.ipynb --output output.ipynb
```

## 4. Package Management in Notebooks

### Install Packages in Notebook

```python
import subprocess
import sys

# Install package
subprocess.check_call([sys.executable, "-m", "pip", "install", "package_name"])
```

Or simpler:

```python
!pip install package_name
```

### Import from Local Modules

```python
import sys
sys.path.append('../')
from module_name import function_name
```

## 5. Troubleshooting

### Kernel Not Showing

**Problem**: Newly created kernel doesn't appear in Jupyter

**Solution**:
```bash
# Refresh kernelspec
jupyter kernelspec list
jupyter kernelspec remove old_kernel
python -m ipykernel install --user --name new_kernel
```

### ImportError in Notebook

**Problem**: `ModuleNotFoundError: No module named 'package'`

**Solution**:
```python
# Check Python version
import sys
print(sys.version)

# Verify package installation
!pip show package_name

# Install if missing
!pip install package_name
```

### Slow Notebook Performance

**Problem**: Notebook runs slowly

**Solutions**:
```python
# Check memory usage
import psutil
process = psutil.Process()
print(process.memory_info().rss / 1024 / 1024, "MB")

# Use %time for profiling
%time result = expensive_operation()

# Use %prun for line profiling
%prun expensive_operation()
```

### Notebook Won't Start

**Problem**: Kernel crashes or won't start

**Solution**:
```bash
# Clear notebook cache
rm -rf ~/.local/share/jupyter/runtime/kernel*

# Restart Jupyter
jupyter notebook --no-browser --port=8888
```

## Best Practices

### 1. Organize Imports

```python
# Standard library
import os, sys, json

# Third-party
import numpy as np
import pandas as pd

# Local modules
from utils import helper_function
```

### 2. Use Markdown Cells Effectively

```markdown
# Section Title

## Subsection

Explain what the code below does.

**Key Points:**
- Point 1
- Point 2
```

### 3. Add Docstrings

```python
def analyze_sequence(sequence: str) -> dict:
    """
    Analyze DNA sequence properties.
    
    Args:
        sequence: DNA sequence string (A, T, G, C)
        
    Returns:
        dict: GC content and length
        
    Example:
        >>> analyze_sequence("ATGC")
        {'gc_content': 0.5, 'length': 4}
    """
    gc = (sequence.count('G') + sequence.count('C')) / len(sequence)
    return {'gc_content': gc, 'length': len(sequence)}
```

### 4. Use Magic Commands

```python
# Timing
%time result = computation()

# Debugging
%debug

# Profiling
%prun expensive_operation()

# Display settings
%matplotlib inline

# Shell commands
!ls -la
```

### 5. Save and Export

```bash
# Save notebook
Ctrl+S (or Cmd+S on Mac)

# Export to HTML
jupyter nbconvert --to html notebook.ipynb

# Export to PDF
jupyter nbconvert --to pdf notebook.ipynb

# Export to Python script
jupyter nbconvert --to script notebook.ipynb
```

---

**Last Updated**: May 2024

