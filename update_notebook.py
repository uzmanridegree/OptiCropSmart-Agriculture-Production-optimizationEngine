import json
from pathlib import Path
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
nb.setdefault('cells', [])
code = [
    "import pandas as pd\n",
    "import numpy as np\n",
    "pd.set_option('max_colwidth', 20)\n",
    "pd.set_option('display.max_columns',None)\n",
    "pd.set_option('display.max_rows',50)\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline\n",
    "plt.rcParams['figure.figsize'] = (12,8)\n",
    "from IPython.core.interactiveshell import InteractiveShell\n",
    "InteractiveShell.ast_node_interactivity = 'all'\n",
    "from ipywidgets import interact\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import confusion_matrix\n",
    "from sklearn.metrics import classification_report\n",
]
if not nb['cells']:
    nb['cells'].append({'cell_type': 'code', 'metadata': {}, 'source': [], 'outputs': [], 'execution_count': None})
cell = nb['cells'][0]
cell['cell_type'] = 'code'
cell['metadata'] = {}
cell['source'] = code
cell['outputs'] = []
cell['execution_count'] = None
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('Notebook updated successfully.')
