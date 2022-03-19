import streamlit as st
import joblib
import os
import pandas as pd
import numpy as np
#import sqlite3
#from monitor_for_app import *
from variables import *
#from datetime import datetime
st.set_page_config(page_title = 'Diabetes prediction')

@st.cache
def load_data():
    df = pd.read_csv('data/diabetes.csv')
    return df

def load_model(model):
	load_model = joblib.load(open(os.path.join(model),"rb"))
	return load_model

# load data
df = load_data()

def main():
    options = ['Homepage', 'Data' ,'Make Prediction', 'Monitoring' ,'About']
    page_option = st.sidebar.selectbox('Options', options)
    
    if page_option == 'Homepage':
        st.title('Diabetes predictor')
        
    elif page_option == 'Data':

        st.title('More informations about dataset')
        st.markdown(data_description, unsafe_allow_html = True)
        with st.expander('Descriptive statistics', expanded = False):
            st.write('Here you can get some statistics for all numeric columns.')
            st.write(df.describe())
        with st.expander('Target values'):
            st.write('We have 35% class 1 observations.')
            st.write(round(df.Outcome.value_counts(normalize = True)*100, 2))
        
    elif page_option == 'Make Prediction':

        st.title('Prediction')
        pregnancies = st.slider('Pregnancies: ', pregnancies_min_value, pregnancies_max_value, 0)
        glucose = st.number_input('Glucose: ', glucose_min_value, glucose_max_value, 100)
        blood_pressure = st.number_input('Blood pressure: ', blood_min_value, blood_max_value, 70)
        skin = st.number_input('Skin Thickness: ', skin_min_value, skin_max_value, 23)
        insulin = st.number_input('Insulin: ', insulin_min_value, insulin_max_value, 30)
        bmi = st.number_input('BMI: ', bmi_min_value, bmi_max_value, 32.0)
        diabetes_function = st.number_input('Diabetes Pedigree Function', diabetes_function_min_value, diabetes_function_max_value, 0.3725)
        age = st.slider('Age: ', age_min_value, age_max_value, 29)
        selected_options = [pregnancies, glucose, blood_pressure, skin, insulin, bmi, diabetes_function, age]
        
        sample_input = np.array(selected_options).reshape(1,-1)
        model = load_model('model/svc.pkl')
        # class prediction
        prediction_class = model.predict(sample_input)
        # proba prediction
        prediction_proba = model.predict_proba(sample_input)
        if st.button('Submit'):
            st.success(f'Pregancies: {pregnancies}')
            st.success(f'Glucose: {glucose}')
            st.success(f'Blood pressure: {blood_pressure}')
            st.success(f'Skin Thickness: {skin}')
            st.success(f'Insulin: {insulin}')
            st.success(f'BMI: {bmi}')
            st.success(f'Diabetes Pedigree Function: {diabetes_function}')
            st.success(f'Age: {age}')
            st.success(f"Result of prediction: {prediction_class[0]}")
            st.success(f"Probability for class 1 is {round(prediction_proba[0,1]*100, 2)}%.")
        
    elif page_option == 'Monitoring':
        st.title('Monitoring')
        
    else:
        st.title('About')
        col1, col2 = st.columns(2)
        
        with col1:
            st.text('Column 1')
        with col2:
            st.text('Column 2')
            
            
        col3, col4, col5 = st.columns(3)
        
        with col3:
            st.text('Column 1')
        with col4:
            st.text('Column 2')
        with col5:
            st.text('Column 3')
        
        col6, col7 = st.columns([3, 1])
        with col6:
            st.text('Column 1')
        with col7:
            st.text('Column 2')
        
    
main()

