import requests
import json
import time
import numpy as np

# url local - definida no app.py - executada pelo Flask
url = 'http://127.0.0.1:5000'

# parâmetros de entrada:
Pregnancies              = [i for i in range(3)]
Glucose                  = np.linspace(60,380,10).tolist()
BloodPressure            = [i for i in range(50,100,10)] 
SkinThickness            = [i for i in range(15,30,3)]
Insulin                  = [i for i in range(20,50,10)]
BMI                      = [i for i in range(28,35,3)]    
DiabetesPedigreeFunction = np.linspace(0.2,0.5,3).tolist()
Age                      = [i for i in range(10,90,20)]



def generate_use_cases():
    for pregnancies in Pregnancies:
        for glucose in Glucose:
            for bloodPressure in BloodPressure:
                for skinThickness in SkinThickness:
                    for insulin in Insulin:
                        for bmi in BMI:
                            for diabetesPedigreeFunction in DiabetesPedigreeFunction:
                                for age in Age:


                                    yield {'Pregnancies':              pregnancies, 
                                           'Glucose':                  glucose, 
                                           'BloodPressure':            bloodPressure,
                                           'SkinThickness':            skinThickness, 
                                           'Insulin':                  insulin,
                                           'BMI':                      bmi, 
                                           'DiabetesPedigreeFunction': diabetesPedigreeFunction, 
                                           'Age':                      age}


if __name__ == '__main__':
    for data in generate_use_cases():   
        print(data)
        data = json.dumps(data)
        
        start = time.time()
        send_request = requests.post(url, data)
        print("tempo de resposta: ",time.time()-start)

        print(send_request.json())