import sys
import os
sys.path.append(os.getcwd())

from flask import Flask,  jsonify, request
import numpy as np
from src.model.model import Diabetes
from src.modulos.parser import parser

app = Flask(__name__)
diabetes = Diabetes()

@app.route('/', methods=['POST'])
def predict(): 
    values = parser(request)
    result = diabetes.predict(values)
    return jsonify(results=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host = "0.0.0.0",port = port, debug=True)

