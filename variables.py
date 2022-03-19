# SECTION HOMEPAGE

import pandas as pd
df = pd.read_csv('data/diabetes.csv')

home_page_text = """
<div style="text-align: justify">Diabetes is due to either the pancreas not producing enough insulin, or the cells of the body not responding properly to the insulin produced. There are three main types of diabetes mellitus.
Type 1 diabetes results from failure of the pancreas to produce enough insulin due to loss of beta cells. This form was previously referred to as "insulin-dependent diabetes mellitus" or "juvenile diabetes". The loss of beta cells is caused by an autoimmune response. The cause of this autoimmune response is unknown.
Type 2 diabetes begins with insulin resistance, a condition in which cells fail to respond to insulin properly. As the disease progresses, a lack of insulin may also develop. This form was previously referred to as "non insulin-dependent diabetes mellitus" or "adult-onset diabetes". The most common cause is a combination of excessive body weight and insufficient exercise.
Gestational diabetes is the third main form, and occurs when pregnant women without a previous history of diabetes develop high blood sugar levels (text FROM WIKIPEDIA).
The aim of this Data App is to predict whether or not the patient has diabetes.</div>

"""
#  SECTION DATA

data_description = """
<div style = "text-align: justify">The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on (FROM KAGGLE).</div>

"""


# SECTION MAKE PREDICTION
# pregnancies options
pregnancies_min_value = int(df['Pregnancies'].min())
pregnancies_max_value = int(df['Pregnancies'].max())
# glucose options
glucose_min_value = int(df['Glucose'].min())
glucose_max_value = int(df['Glucose'].max())
# blood pressure options
blood_min_value = int(df['BloodPressure'].min())
blood_max_value = int(df['BloodPressure'].max())
# Skin Thickness options
skin_min_value = int(df['SkinThickness'].min())
skin_max_value = int(df['SkinThickness'].max())
# insulin options
insulin_min_value = int(df['Insulin'].min())
insulin_max_value = int(df['Insulin'].max())
# BMI options
bmi_min_value = float(df['BMI'].min())
bmi_max_value = float(df['BMI'].max())
# Diabetes Pedigree Function options
diabetes_function_min_value = float(df['DiabetesPedigreeFunction'].min())
diabetes_function_max_value = float(df['DiabetesPedigreeFunction'].max())
# Age options
age_min_value = int(df['Age'].min())
age_max_value = int(df['Age'].max())

# SECTION ABOUT
about_text = """
<div style="text-align: justify">Diabetes mellitus, commonly known as diabetes, is a group of metabolic disorders characterized by a high blood sugar level over a prolonged period of time.Symptoms often include frequent   urination, increased thirst and increased appetite. If left untreated, diabetes can cause many health complications. Acute complications can include diabetic ketoacidosis, hyperosmolar hyperglycemic state, or death. Serious long-term complications include cardiovascular disease, stroke, chronic kidney disease, foot ulcers, damage to the nerves, damage to the eyes and cognitive impairment (from Wikipedia).    


Thus, the purpose of this application is to predict whether or not the patient has diabetes. For didactic purposes we use only the SVM model.</div>
"""