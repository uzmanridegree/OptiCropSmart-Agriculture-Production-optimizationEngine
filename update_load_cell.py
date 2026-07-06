import json
from pathlib import Path
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
if len(nb.get('cells', [])) < 2:
    while len(nb['cells']) < 2:
        nb['cells'].append({'cell_type': 'code', 'metadata': {}, 'source': [], 'outputs': [], 'execution_count': None})
cell = nb['cells'][1]
cell['cell_type'] = 'code'
cell['metadata'] = {}
cell['source'] = [
    "data = pd.read_csv('Crop_recommendation.csv')\n",
    "data.head()\n",
]
cell['outputs'] = []
cell['execution_count'] = None
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('Notebook second cell updated with CSV load code.')
