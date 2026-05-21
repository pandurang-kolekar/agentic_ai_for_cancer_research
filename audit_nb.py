import glob, json, os

markers = ['Add your','placeholder','TODO','Content goes here','Exercise 1: [','{chapter_num}','Pass # TODO','Your code goes here']
stats = {"COMPLETE": 0, "PARTIAL": 0, "TEMPLATE": 0}

print(f"{'Chapter':<15} | {'Tot':>3} | {'MD':>3} | {'Code':>4} | {'Exec':>4} | {'Verdict'}")
print("-" * 55)

for nb_path in sorted(glob.glob("chapters/*/notebook.ipynb")):
    chapter = nb_path.split(os.sep)[1]
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except:
        continue
    
    cells = nb.get('cells', [])
    tot = len(cells)
    md = len([c for c in cells if c['cell_type'] == 'markdown'])
    code = [c for c in cells if c['cell_type'] == 'code']
    num_code = len(code)
    exec_code = len([c for c in code if c.get('execution_count') is not None])
    
    found_marker = False
    nb_str = json.dumps(nb)
    for m in markers:
        if m in nb_str:
            found_marker = True
            break
                                          verdict = "TEMPLATE"
    elif num_code >= 5:
        verdict = "COMPLETE"
    else:
        verdict = "PARTIAL"
    
    stats[verdict] += 1
    print(f"    print(f"    print(f"    print(f"    print(f"   | {    print(f"    print(f"    print(f"    print(f"    print(f"   | {    print(f"    print(f" :     print(f"  L']}, TEMPLATE: {stats['TEMPLATE']}")
