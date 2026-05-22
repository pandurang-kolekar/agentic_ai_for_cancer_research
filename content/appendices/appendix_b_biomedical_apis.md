# Appendix B: APIs and Biomedical Databases

## Overview

This appendix covers major biomedical databases and their APIs for accessing genomic, clinical, and scientific data.

## Contents

1. NCBI Resources
2. UniProt
3. PubMed and Literature
4. ClinicalTrials.gov
5. Ensembl
6. gnomAD
7. Disease Databases
8. Best Practices for API Usage

## 1. NCBI Resources

### Entrez E-utilities

```python
from Bio import Entrez

Entrez.email = "your@email.com"

# Search for genes
handle = Entrez.esearch(db="gene", term="TP53 AND human")
record = Entrez.read(handle)

# Fetch sequences
handle = Entrez.efetch(db="nucleotide", id="NZ_AACY020159625", rettype="fasta")
print(handle.read().decode())
```

### BLAST

```python
from Bio.Blast import NCBIWWW, NCBIXML

# Run BLAST search
result_handle = NCBIWWW.qblast("blastp", "nr", sequence)
blast_record = NCBIXML.read(result_handle)

for alignment in blast_record.alignments:
    print(alignment.title)
```

## 2. UniProt

### Protein Information

```python
import requests

# Get protein info
response = requests.get(
    "https://www.uniprot.org/api/uniprotkb/P12345.json"
)
protein = response.json()
print(protein['uniProtkbId'])
```

## 3. PubMed and Literature

### PyMed Library

```python
from pymed import PubMed

pubmed = PubMed(tool="MyApp", email="user@example.com")
results = pubmed.query("BRCA1 mutations cancer")

for article in results:
    print(article.title)
```

### RESTful API

```python
import requests

# Search PubMed
params = {
    'db': 'pubmed',
    'term': 'cancer immune therapy',
    'retmode': 'json',
    'retmax': 10
}

response = requests.get(
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
    params=params
)
data = response.json()
```

## 4. ClinicalTrials.gov

### Trial Search API

```python
import requests

params = {
    'query.cond': 'breast cancer',
    'query.recr': 'OPEN',
    'pageSize': 20,
    'countTotal': True
}

response = requests.get(
    "https://clinicaltrials.gov/api/query/full_studies",
    params=params
)
trials = response.json()

for study in trials['FullStudiesResponse']['NStudiesReturned']:
    print(study['ProtocolSection']['IdentificationModule']['OfficialTitle'])
```

## 5. Ensembl

### Ensembl REST API

```python
import requests, json

# Get gene info
response = requests.get(
    "https://rest.ensembl.org/lookup/id/ENSG00000141510?expand=1",
    headers={'Content-Type': 'application/json'}
)

data = response.json()
print(data['display_name'], data['description'])
```

## 6. gnomAD

### Variant Frequency Database

```python
import requests

# Query gnomAD
query = """
{
  variant(dataset: gnomad_r2_1, id: "1-1-A-G") {
    rsid
    gnomad {
      ac
      an
      af
    }
  }
}
"""

response = requests.post(
    "https://gnomad.broadinstitute.org/api",
    json={'query': query}
)
```

## 7. Disease Databases

### PharmGKB

Pharmacogenomics knowledge base with drug-gene interactions

```python
# API example
import requests

response = requests.get(
    "https://api.pharmgkb.org/v1/download?fileName=genes.zip"
)
```

### The Protein Data Bank (PDB)

Structure data

```python
# Download PDB structure
from Bio.PDB import PDBParser, PDBList

pdbl = PDBList()
pdbl.retrieve_pdb_file("1BNA", file_format="pdb")
```

## 8. Best Practices for API Usage

### Rate Limiting

```python
import time
import requests
from functools import wraps

def rate_limited(max_per_second=1):
    min_interval = 1.0 / max_per_second
    last_called = [0.0]
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = min_interval - elapsed
            if wait_time > 0:
                time.sleep(wait_time)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

@rate_limited(max_per_second=2)
def query_api(endpoint):
    return requests.get(endpoint)
```

### Error Handling

```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

response = requests_retry_session().get("https://api.example.com/data")
```

## Key Databases Summary

| Database | Type | API | Key Use |
|----------|------|-----|---------|
| NCBI | Gene/Sequence | Yes | Sequence search, annotation |
| UniProt | Protein | Yes | Protein information |
| PubMed | Literature | Yes | Scientific publications |
| ClinicalTrials.gov | Clinical | Yes | Trial information |
| Ensembl | Genomics | Yes | Gene annotation |
| gnomAD | Variants | Yes | Population frequencies |
| PDB | Structures | Yes | 3D structures |
| PharmGKB | Pharmacogenomics | Yes | Drug-gene interactions |

---

**Last Updated**: May 2024

