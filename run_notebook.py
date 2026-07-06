import json
from pathlib import Path
try:
    import nbformat
    from nbclient import NotebookClient
except ImportError as e:
    raise SystemExit(f'Missing dependency: {e}')
path = Path('data_collection_analysis/dataanalysis.ipynb')
nb = nbformat.read(path, as_version=4)
client = NotebookClient(nb, timeout=600, kernel_name='python3')
nb = client.execute()
nbformat.write(nb, path)
print('Notebook executed successfully.')
