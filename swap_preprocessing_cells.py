import json
from pathlib import Path
path = Path('data_collection_analysis/preprocessing.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
# Swap the boxplot and filtering cells to match the image code order
if len(nb.get('cells', [])) >= 8:
    boxplot_cell = nb['cells'][6]
    filter_cell = nb['cells'][7]
    nb['cells'][6]['source'], nb['cells'][7]['source'] = filter_cell.get('source', []), boxplot_cell.get('source', [])
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('Swapped preprocessing notebook cells.')
