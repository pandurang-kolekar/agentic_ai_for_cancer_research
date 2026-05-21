import json
import glob
import os

scaffold_markers = ['Add your', 'placeholder', 'TODO', 'Content goes here', 'Exercise 1: [', '{chapter_num}']

results = []
sanity_list = []

notebooks = glob.glob('chapters/*/notebook.ipynb')

for nb_path in notebooks:
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        print(f"Error reading {nb_path}: {e}")
        continue

    cells = nb.get('cells', [])
    cell_count = len(cells)
    markdown_count = sum(1 for c in cells if c['cell_type'] == 'markdown')
    code_cells = [c for c in cells if c['cell_type'] == 'code']
    code_count = len(code_cells)
    executed_count = sum(1 for c in code_cells if c.get('execution_count') is not None)

    has_scaffold = False
    for cell in cells:
        source = "".join(cell.get('source', []))
        if any(marker in source for marker in scaffold_markers):
            has_scaffold = True
            break
    
    if has_scaffold:
        verdict = "TEMP        veel   code_coun                   verdict = "TEMP        veel   code_coun                   verdict = "TEMP        veel   code_cou nb_path,
        'c        'c     nt,        'c        'c     nt,        'c        'c e': code_count,
        'executed': ex        'executed': ex        'executed': ex        'ef cell_count <= 2:
        sanity_list.append(nb_path)

# Print Table
header = f"{'Notebook Path':<60} | {'Cells':<5} | {'MD':<3} | {'Code':<4} | {'Exec':<4} | {'Verdict':<8}"
print(header)
print("-" * len(header))
for r in sorted(results, key=lambda x: x['pafor r in sorted(results, key=lambda x: x['pafor r in sorted(rekdown']:<3} | {r['code']:<4} | {r['for r in sorted(results, key=lambda x: x['pafor r in sorted(results, key=lambda x: LETE': 0, 'PARTIAL': 0}
for r in results:
    totals[r['verdict']] += 1

print("\nBucket Totals:")
for for for for for for for for for for for for for for for for anityfor for for for for for for fst for for for for ):")
                    ty_list:
        print(path)
