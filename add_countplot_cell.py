import json
from pathlib import Path
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
if len(nb.get('cells', [])) < 5:
    while len(nb['cells']) < 5:
        nb['cells'].append({'cell_type': 'code', 'metadata': {}, 'source': [], 'outputs': [], 'execution_count': None})
cell = nb['cells'][4]
cell['cell_type'] = 'code'
cell['metadata'] = {}
cell['source'] = [
    "sns.countplot(data)\n",
    "plt.show()\n",
]
cell['outputs'] = []
cell['execution_count'] = None
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('Inserted countplot cell.')
