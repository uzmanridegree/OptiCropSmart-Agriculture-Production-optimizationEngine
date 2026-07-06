# pyrefly: ignore [missing-import]
import nbformat as nbf

nb = nbf.v4.new_notebook()

text = 'Preprocessing'

code1 = 'import pandas as pd\ndata = pd.read_csv("Crop_recommendation.csv")'

code2 = 'data.info()'

code3 = 'data.shape'

nb['cells'] = [
    nbf.v4.new_markdown_cell(text),
    nbf.v4.new_code_cell(code1),
    nbf.v4.new_code_cell(code2),
    nbf.v4.new_code_cell(code3)
]

nbf.write(nb, 'preprocessing.ipynb')
