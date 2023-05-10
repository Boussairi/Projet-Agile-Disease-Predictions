# -*- coding: utf-8 -*-


import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open("C:/Users/Xps/Desktop/S4/Autoformation/Disease prediction/diabetes_model.sav", 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
     # Convert inputs to numeric format
pregnancies = int(pregnancies)
glucose_level = int(glucose_level)
blood_pressure = int(blood_pressure)
skin_thickness = int(skin_thickness)
insulin_level = int(insulin_level)
bmi = float(bmi)
diabetes_pedigree_function = float(diabetes_pedigree_function)
age = int(age)

# Determine risk of diabetes based on inputs
if glucose_level > 140:
    st.write('Your glucose level is high. You should consult with a doctor to determine if you are at risk for developing diabetes. In the meantime, try to limit your intake of sugary foods and drinks, and increase your physical activity.')
elif bmi > 30:
    st.write('Your BMI is high. You should consult with a doctor to determine if you are at risk for developing diabetes. In the meantime, try to incorporate more fruits and vegetables into your diet, and increase your physical activity.')
elif age > 45:
    st.write('Your age puts you at a higher risk for developing diabetes. You should consult with a doctor to determine if you are at risk. In the meantime, try to limit your intake of sugary foods and drinks, and increase your physical activity.')
elif pregnancies > 0:
    st.write('Your history of pregnancies puts you at a higher risk for developing diabetes. You should consult with a doctor to determine if you are at risk. In the meantime, try to incorporate more fruits and vegetables into your diet, and increase your physical activity.')
else:
    st.write('Based on your inputs, you appear to be at a lower risk for developing diabetes. However, it is always a good idea to maintain a healthy lifestyle to reduce your risk. Try to incorporate more fruits and vegetables into your diet, limit your intake of sugary foods and drinks, and increase your physical activity. It is also recommended that you schedule regular check-ups with your doctor to monitor your health.')    
    
# Determine risk of heart disease based on inputs
if gender == 'Male' and age > 45:
    if blood_pressure > 130 or glucose_level > 100 or bmi > 25:
        st.write('You appear to be at risk for developing heart disease. It is important to maintain a healthy lifestyle by eating a balanced diet, exercising regularly, quitting smoking (if applicable), and reducing stress.')
elif gender == 'Female' and age > 55:
    if blood_pressure > 130 or glucose_level > 100 or bmi > 25:
        st.write('You appear to be at risk for developing heart disease. It is important to maintain a healthy lifestyle by eating a balanced diet, exercising regularly, quitting smoking (if applicable), and reducing stress.')
else:
    st.write('Based on your inputs, you appear to be at a lower risk for developing heart disease. However, it is still important to maintain a healthy lifestyle to reduce your risk of developing heart disease.')
    
# Determine risk of Parkinson's disease based on inputs
if age > 60 and insulin_level < 30:
    st.write('Your insulin level is low, and you are above the age of 60. You should consult with a doctor to determine if you are at risk for developing Parkinson\'s disease.')
else:
    st.write('Based on your inputs, you appear to be at a lower risk for developing Parkinson\'s disease. However, it is always a good idea to maintain a healthy lifestyle to reduce your risk.')    
    
    
    
    
    
    
    
    
    
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  
