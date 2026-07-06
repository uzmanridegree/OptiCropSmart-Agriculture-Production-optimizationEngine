import json
from pathlib import Path
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
if len(nb.get('cells', [])) >= 2:
    cell = nb['cells'][1]
    src = ''.join(cell.get('source', []))
    if "df = data" not in src:
        new_source = []
        for line in cell.get('source', []):
            new_source.append(line)
            if line.startswith("data = pd.read_csv"):
                new_source.append("df = data\n")
        cell['source'] = new_source
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('Defined df alias in second cell.')
