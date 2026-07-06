import json
from pathlib import Path
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
for i, cell in enumerate(nb.get('cells', []), start=1):
    print(f'CELL {i} ({cell.get("cell_type")}) source lines: {len(cell.get("source", []))}')
    for line in cell.get('source', []):
        print(repr(line))
    print('---')
