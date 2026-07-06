#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load and prepare data
data = pd.read_csv('Crop_recommendation.csv')
x = data.drop(['label'], axis=1)


# In[2]:


#el-bow method used to find out no of clusters and detemine the optimum number of clusters within the dataset.
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize']=(10,4)
wcss=[]
for i in range(1,11):
    km=KMeans(n_clusters=i,init="k-means++",max_iter=300,n_init=10,random_state=0)
    km.fit(x)
    wcss.append(km.inertia_)

plt.plot(range(1,11),wcss)
plt.title("The Elbow method",fontsize=20)
plt.xlabel("No of clusters")
plt.ylabel("wcss")
plt.show()


# In[3]:


km=KMeans(n_clusters=4,init="k-means++",max_iter=300,n_init=10,random_state=0)
y_means=km.fit_predict(x)

a=data['label']
y_means=pd.DataFrame(y_means)
z=pd.concat([y_means,a],axis=1)
z=z.rename(columns={0:'cluster'})

print("lets check the results after applying the K-Means clustering analysis \n")
print("Crops in First cluster:",z[z['cluster']==0]['label'].unique())
print("_________________________________________________________________")

print("Crops in Second cluster:",z[z['cluster']==1]['label'].unique())

print("_________________________________________________________________")

print("Crops in Third cluster:",z[z['cluster']==2]['label'].unique())

print("_________________________________________________________________")

print("Crops in Fourth cluster:",z[z['cluster']==3]['label'].unique())


# In[4]:


# Load preprocessing data with train-test split
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv('Crop_recommendation.csv')
y = data['label']
x = data.drop(['label'], axis=1)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


# In[5]:


# Scale the data for better convergence
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

print("Data scaled successfully")
print("x_train_scaled shape:", x_train_scaled.shape)
print("x_test_scaled shape:", x_test_scaled.shape)


# In[6]:


# LOGISTIC REGRESSION
from sklearn.linear_model import LogisticRegression

model=LogisticRegression(max_iter=1000)
model.fit(x_train_scaled,y_train)
y_pred=model.predict(x_test_scaled)

print("Logistic Regression Model trained successfully")
print("Predictions shape:", y_pred.shape)


# In[7]:


# Model Evaluation
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

train_accuracy = model.score(x_train_scaled, y_train)
test_accuracy = accuracy_score(y_test, y_pred)

print("Model Evaluation Results:")
print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy: {test_accuracy:.4f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
print(f"Recall: {recall_score(y_test, y_pred, average='weighted'):.4f}")
print(f"F1-Score: {f1_score(y_test, y_pred, average='weighted'):.4f}")


# In[8]:


from sklearn.metrics import classification_report
cr=classification_report(y_test,y_pred)
print(cr)


# In[9]:


import numpy as np

# Make prediction for a given climatic condition
# Features: [N, P, K, temperature, humidity, ph, rainfall]
input_features = np.array([[105,35,40,25,64,7,160]])

# Scale the input using the same scaler used for training
input_scaled = scaler.transform(input_features)

# Make prediction
prediction = model.predict(input_scaled)

print("The suggested crop for given climatic condition is: ", prediction)


# In[10]:


import pickle
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))


# In[ ]:


import pickle
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

