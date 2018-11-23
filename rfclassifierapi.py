# Creating api for RF classifier

import pickle
from flask import Flask, request
import numpy as np
import pandas as pd

with open('D:\Data Science Class Files\ML Deployment\\rf.pkl','rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

labels = ['setosa', 'versicolor', 'virginica']

@app.route('/predict')
def predict_iris():
    
    s_length = request.args.get('s_length')
    s_width = request.args.get('s_width')
    p_length = request.args.get('p_length')
    p_width = request.args.get('p_width')
    
    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    
    return labels[prediction[0]]

@app.route('/predict_file', methods = ['POST'])
def predict_iris_file():
    
    input_data = pd.read_csv(request.files.get('input_data'), header = None, encoding ='latin1')
    predictions = model.predict(input_data)
    return str(list(predictions))
    
if __name__ == '__main__':
    app.run()
