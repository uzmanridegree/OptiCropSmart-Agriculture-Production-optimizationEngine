# pyrefly: ignore [missing-import]
import nbformat as nbf
with open('preprocessing.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

code = '''print("Summer crops")
print(data[(data['temperature']>30) & (data['humidity']>50)]['label'].unique())
print("-----------------------------------")
print("Winter crops")
print(data[(data['temperature']<20) & (data['humidity']>30)]['label'].unique())
print("-----------------------------------")
print("Rainy crops")
print(data[(data['rainfall']>200) & (data['humidity']>50)]['label'].unique())
print("-----------------------------------")'''

nb.cells.append(nbf.v4.new_code_cell(code))

with open('preprocessing.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
