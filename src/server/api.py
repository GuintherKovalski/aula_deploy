import sys
sys.path.append("/home/pacer/Desktop/DigitalHouse/aulas_16_18/aula_deploy")

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
    app.run(port = 5000, debug=True)

