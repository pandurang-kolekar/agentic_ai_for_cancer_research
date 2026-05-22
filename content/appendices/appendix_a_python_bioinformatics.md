# Appendix A: Python for Bioinformatics

## Overview

This appendix provides essential Python programming concepts and libraries for bioinformatics applications.

## Contents

1. Python Basics for Scientists
2. NumPy for Numerical Computing
3. Pandas for Data Manipulation
4. Working with Biological Sequences
5. File Formats in Bioinformatics
6. Performance Optimization
7. Debugging and Testing

## 1. Python Basics for Scientists

### Virtual Environments

```python
# Create and activate virtual environment
python -m venv bioenv
source bioenv/bin/activate  # macOS/Linux
```

### Key Libraries

```python
# Import common libraries
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple, Optional
import json, csv, pickle
```

## 2. NumPy for Numerical Computing

Working with arrays for genomic data:

```python
import numpy as np

# One-hot encoding for DNA sequences
def one_hot_encode(sequence):
    mapping = {'A': [1, 0, 0, 0],
               'T': [0, 1, 0, 0],
               'G': [0, 0, 1, 0],
               'C': [0, 0, 0, 1]}
    return np.array([mapping[base] for base in sequence])

# Example usage
seq = "ATGC"
encoded = one_hot_encode(seq)
```

## 3. Pandas for Data Manipulation

Working with genomic datasets:

```python
import pandas as pd

# Load VCF-like data
df = pd.read_csv('variants.csv')

# Filtering
high_impact = df[df['IMPACT'] == 'HIGH']

# Grouping
by_gene = df.groupby('GENE')['AF'].mean()
```

## 4. Working with Biological Sequences

### BioPython

```python
from Bio import SeqIO, Seq, SeqUtils

# Read FASTA files
for record in SeqIO.parse("sequences.fasta", "fasta"):
    print(record.id, len(record.seq))

# Translate DNA to protein
dna = Seq.Seq("ATGAAATAG")
protein = dna.translate()
```

## 5. File Formats in Bioinformatics

### FASTA

```python
from Bio import SeqIO

# Write FASTA
SeqIO.write([record], "output.fasta", "fasta")
```

### VCF (Variant Call Format)

```python
import vcf

vcf_reader = vcf.Reader(filename='variants.vcf')
for record in vcf_reader:
    print(record.CHROM, record.POS)
```

### SAM/BAM (Sequence Alignment Map)

```python
import pysam

samfile = pysam.AlignmentFile("file.bam", "rb")
for aligned_segment in samfile:
    print(aligned_segment.query_name, aligned_segment.query_sequence)
```

## 6. Performance Optimization

### Use Vectorization

```python
# Slow: Python loops
result = []
for i in range(1000000):
    result.append(i ** 2)

# Fast: NumPy vectorization
result = np.arange(1000000) ** 2
```

### Multiprocessing

```python
from multiprocessing import Pool

def process_sequence(seq):
    return len(seq)

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        results = pool.map(process_sequence, sequences)
```

## 7. Debugging and Testing

### Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Processing sequence")
logger.error("Sequence not found")
```

### Unit Testing

```python
import unittest

class TestBioFunctions(unittest.TestCase):
    def test_gc_content(self):
        seq = "ATGC"
        gc = (seq.count('G') + seq.count('C')) / len(seq)
        self.assertEqual(gc, 0.5)
```

## Resources

- [BioPython Documentation](https://biopython.org/)
- [NumPy Guide](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/)

---

**Last Updated**: May 2024

