# OptiCrop - Smart Agricultural Optimization Engine

OptiCrop is an intelligent agricultural recommendation system that leverages machine learning and data science to help farmers make informed decisions about crop selection. By analyzing environmental factors and soil properties, the system provides personalized crop recommendations to maximize yield and resource efficiency.

## 🌟 Key Features
- **Data-Driven Recommendations**: Predicts the best crop based on soil and environmental parameters.
- **High Accuracy ML Model**: Powered by a Logistic Regression model trained on 2,200+ samples, achieving 96.36% test accuracy.
- **Modern User Interface**: A clean, responsive web application built with a premium glassmorphism design for a seamless user experience.
- **Extensive Crop Support**: Provides recommendations for 22 different crop varieties including cereals, pulses, and cash crops.

## 🛠️ Technology Stack
- **Backend Framework**: Python (Flask)
- **Machine Learning**: scikit-learn (Logistic Regression, K-Means clustering)
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML5, CSS3, Google Fonts (Outfit)

## 📊 Dataset Information
- **Total Samples**: 2,200 agricultural records
- **Environmental Factors (Features)**: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH Level, Rainfall
- **Crop Classes**: 22 varieties

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KusumaReddyYarram/opti-crop.git
   cd opti-crop
   ```

2. **Install dependencies**:
   Ensure you have the required Python libraries installed:
   ```bash
   pip install flask scikit-learn pandas numpy jupyter
   ```

3. **Generate Models (Optional if models exist)**:
   Navigate to the `data_collection_analysis` folder and execute the notebook `model building.ipynb` (or the converted `model building.py` script) to generate `model.pkl` and `scaler.pkl`.

4. **Start the Web Application**:
   Navigate to the `data_collection_analysis` folder and run the Flask server:
   ```bash
   cd data_collection_analysis
   python app.py
   ```
   
5. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

## 📈 Objective
Our mission is to empower farmers with data-driven insights that optimize agricultural production, improve resource efficiency, and promote sustainable farming practices.
