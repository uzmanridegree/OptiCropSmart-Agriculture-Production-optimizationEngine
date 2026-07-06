import json
from pathlib import Path
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
# Fix the data loading cell
if len(nb.get('cells', [])) >= 2:
    cell = nb['cells'][1]
    source = [
        "data = pd.read_csv('../Crop_recommendation.csv')\n",
        "df = data\n",
        "data.head()\n",
    ]
    cell['source'] = source
# Fix countplot cell to use data keyword
if len(nb.get('cells', [])) >= 5:
    cell = nb['cells'][4]
    cell['source'] = [
        "sns.countplot(data=data)\n",
        "plt.show()\n",
    ]
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('Notebook path and countplot fixed.')
