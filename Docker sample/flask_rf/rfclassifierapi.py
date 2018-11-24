# Creating api for RF classifier

import pickle
from flask import Flask, request
from flasgger import Swagger
import numpy as np
import pandas as pd

with open('\var\www\rfclassifierapi\rf.pkl','rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)
swagger = Swagger(app)

labels = ['setosa', 'versicolor', 'virginica']

@app.route('/predict')
def predict_iris():
    """Example endpoint returning a perdiction for iris
    ---
    parameters:
     - name: s_length
       in: query
       type: number
       required: True
     - name: s_width
       in: query
       type: number
       required: True
     - name: p_length
       in: query
       type: number
       required: True
     - name: p_width
       in: query
       type: number
       required: True
    """
    s_length = request.args.get('s_length')
    s_width = request.args.get('s_width')
    p_length = request.args.get('p_length')
    p_width = request.args.get('p_width')
    
    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    
    return labels[prediction[0]]

@app.route('/predict_file', methods = ['POST'])
def predict_iris_file():
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
     - name: input_data
       in: formData
       type: file
       required: True
    """
    input_data = pd.read_csv(request.files.get('input_data'), header = None)
    # variable name and string name must be the same.
    predictions = model.predict(input_data)
    return str(list(predictions))
    
if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 8180, debug = True, use_evalex = False,threaded = True)