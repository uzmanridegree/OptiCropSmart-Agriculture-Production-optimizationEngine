import json
from pathlib import Path
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
plot_code = [
    "fig, axes = plt.subplots(2, 4, figsize=(20, 10))\n",
    "columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']\n",
    "titles = [\n",
    "    'Ratio of Nitrogen',\n",
    "    'Ratio of Phosphorous',\n",
    "    'Ratio of Potassium',\n",
    "    'Ratio of Temperature',\n",
    "    'Ratio of Humidity',\n",
    "    'Ratio of PH',\n",
    "    'Ratio of Rainfall'\n",
    "]\n",
    "for ax, col, title in zip(axes.flat, columns, titles):\n",
    "    sns.histplot(data[col], kde=True, ax=ax, stat='density', alpha=0.6)\n",
    "    ax.set_title(title)\n",
    "    ax.set_xlabel('')\n",
    "    ax.set_ylabel('Density')\n",
    "for empty_ax in axes.flat[len(columns):]:\n",
    "    empty_ax.axis('off')\n",
    "plt.suptitle('Distribution of agricultural conditions', fontsize=18)\n",
    "plt.tight_layout(rect=[0, 0, 1, 0.95])\n",
    "plt.show()\n",
]
if len(nb.get('cells', [])) < 3:
    while len(nb['cells']) < 3:
        nb['cells'].append({'cell_type': 'code', 'metadata': {}, 'source': [], 'outputs': [], 'execution_count': None})
cell = nb['cells'][2]
cell['cell_type'] = 'code'
cell['metadata'] = {}
cell['source'] = plot_code
cell['outputs'] = []
cell['execution_count'] = None
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('Added plotting code cell to notebook.')
