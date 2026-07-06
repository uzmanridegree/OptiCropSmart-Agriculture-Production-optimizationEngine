import nbformat as nbf

# 1. Update model building.ipynb
with open('model building.ipynb', 'r', encoding='utf-8') as f:
    nb1 = nbf.read(f, as_version=4)

code_to_append = '''import pickle
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))
'''
nb1.cells.append(nbf.v4.new_code_cell(code_to_append))

with open('model building.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb1, f)

# 2. Update Application building.ipynb
with open('Application building.ipynb', 'r', encoding='utf-8') as f:
    nb2 = nbf.read(f, as_version=4)

new_app_code = '''import numpy as np
from flask import Flask, request, render_template
import pickle

app=Flask(__name__)

model=pickle.load(open("model.pkl",'rb'))
scaler=pickle.load(open("scaler.pkl",'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/findyourcrop')
def findyourcrop():
    return render_template('findyourcrop.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features= [float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    features_scaled = scaler.transform(features)
    prediction=model.predict(features_scaled)
    
    output = prediction[0]
    return render_template('findyourcrop.html',prediction_text='Best crop for given conditions is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
'''

nb2.cells[0].source = new_app_code

with open('Application building.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb2, f)
