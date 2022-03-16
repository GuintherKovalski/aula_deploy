import pandas as pd
from flask import Flask, jsonify, request
import pickle
import numpy as np

# load model
model = pickle.load(open('model/svc.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])
def predict():
    
    # get data
    data = request.get_json(force=True)
    data = dict(data)
    
    values = []
    for key in data:
        values.append(data[key])
    values = np.array(values).reshape(1, -1) 
    
    result = model.predict(values)

    output = {'results': int(result[0])}
    
    print(output)
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)

