import json
from pathlib import Path
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
if len(nb.get('cells', [])) < 4:
    while len(nb['cells']) < 4:
        nb['cells'].append({'cell_type': 'code', 'metadata': {}, 'source': [], 'outputs': [], 'execution_count': None})
cell = nb['cells'][3]
cell['cell_type'] = 'code'
cell['metadata'] = {}
cell['source'] = [
    "plt.subplot(2, 4, 7)\n",
    "sns.scatterplot(x=data['humidity'], y=data['label'])\n",
    "plt.xlabel('humidity')\n",
    "plt.ylabel('label')\n",
    "plt.title('Humidity vs Crop Label')\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
]
cell['outputs'] = []
cell['execution_count'] = None
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('Inserted humidity vs label scatterplot cell.')
