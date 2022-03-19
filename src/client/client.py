import requests
import json
import time

# url local - definida no app.py - executada pelo Flask
url = 'https://aula-deploy-dia-18.herokuapp.com/'

request_json = {'Pregnancies':              3.0, 
                'Glucose':                  100.0, 
                'BloodPressure':            70.0,
                'SkinThickness':            23.0, 
                'Insulin':                  30.0,
                'BMI':                      32.0, 
                'DiabetesPedigreeFunction': 0.3725, 
                'Age':                      25.0}

if __name__ == '__main__':
    data = json.dumps(request_json) 
    send_request = requests.post(url, data)
    #print(dir(send_request))
    print(send_request)
    print(json.loads(send_request.text))
    
