import numpy as np
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

# Configure the path to your project directory
path = os.path.dirname(os.path.abspath(__file__)) + "/"

# Load the trained model and scaler
try:
    model = pickle.load(open(path + "model.pkl", 'rb'))
    scaler = pickle.load(open(path + "scaler.pkl", 'rb'))
except FileNotFoundError as e:
    print(f"Warning: {e}. Please run the model building notebook to create model.pkl and scaler.pkl.")
    model = None
    scaler = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/findyourcrop')
def findyourcrop():
    return render_template('findyourcrop.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return render_template('findyourcrop.html', 
                             prediction_text='Error: Model not loaded. Please ensure model.pkl and scaler.pkl exist.')
    
    try:
        # Extract form values as float array
        int_features = [float(x) for x in request.form.values()]
        features = [np.array(int_features)]
        
        # Scale the features using the scaler
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)
        output = prediction[0]
        
        # Return result
        return render_template('findyourcrop.html', 
                             prediction_text='Best crop for given conditions is {}'.format(output))
    except Exception as e:
        return render_template('findyourcrop.html', 
                             prediction_text='Error in prediction: {}'.format(str(e)))

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
