import pickle

import numpy as np

class Diabetes:
    def __init__(self):
        # load model
        self.model = pickle.load(open('model/svc.pkl','rb'))
        self.significado = ["Negativa","Positivo"]

    def predict(self,values:np.ndarray)-> dict:

        """
        #TODO predições a partir de batch
        #TODO gerar receber o nome da pessoa


        Classificar se a pessoa tem diabetes [Positivo] 
        ou não [Negativo]

        --------------------------------------------------
        Parameters:
            Numpy array unidimensional com formato (1,8)
            cada uma das colunas significa:

                Pregnancies              
                Glucose                  
                BloodPressure           
                SkinThickness             
                Insulin                  
                BMI                       
                DiabetesPedigreeFunction
                Age 

            Indexadas pela posição no array
        -----------------------------
        Retorna
            Um dicionário contendo o resultado da classificação

        """

        result = self.model.predict(values)
        

        output = {'results': self.significado[int(result[0])]}

        return output