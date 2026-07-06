import json
from pathlib import Path
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
for i, cell in enumerate(nb.get('cells', []), 1):
    if cell.get('cell_type') != 'code':
        continue
    src = ''.join(cell.get('source', []))
    if 'df' in src:
        print(f'CELL {i}:')
        print(src)
        print('----')
