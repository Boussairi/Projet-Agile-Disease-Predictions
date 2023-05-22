# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: Hamza
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models


diabetes_model = pickle.load(open(r"diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open(r"heart_disease_model.sav", 'rb'))

parkinsons_model = pickle.load(open(r"parkinsons_model.sav", 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        Pregnancies=float(Pregnancies)
        Glucose=float(Glucose)
        BloodPressure=float(BloodPressure)
        SkinThickness=float(SkinThickness)
        Insulin=float(Insulin)
        BMI=float(BMI)
        Age=float(Age)
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
          # Determine risk of diabetes based on inputs
            if (int(Glucose )> 140):
                st.write('- Your glucose level is high. You should consult with a doctor to determine if you are at risk for developing diabetes. In the meantime, try to limit your intake of sugary foods and drinks, and increase your physical activity.')
            if (int(BMI) > 30):
                st.write('- Your BMI is high. You should consult with a doctor to determine if you are at risk for developing diabetes. In the meantime, try to incorporate more fruits and vegetables into your diet, and increase your physical activity.')
            # Recommandation basée sur l'âge
            if (int(Age) > 45):
                st.write('- Your age puts you at a higher risk for developing diabetes. You should consult with a doctor to determine if you are at risk. In the meantime, try to limit your intake of sugary foods and drinks, and increase your physical activity.')
            if (int(Pregnancies) > 5):
                st.write('- Your history of pregnancies puts you at a higher risk for developing diabetes. You should consult with a doctor to determine if you are at risk. In the meantime, try to incorporate more fruits and vegetables into your diet, and increase your physical activity.')
             
            # Recommandation basée sur la pression artérielle
            if int(BloodPressure) > 130:
                st.write("- Votre pression artérielle est élevée . Il est recommandé de surveiller régulièrement votre tension artérielle et de consulter un médecin pour évaluer votre risque de développer des problèmes cardiovasculaires.")

            # Recommandation basée sur le taux d'insuline
            if int(Insulin) < 10:
                st.write("- Votre taux d'insuline est inférieur à la normale. Cela peut indiquer une résistance à l'insuline ou d'autres problèmes métaboliques. Il est recommandé de consulter un médecin pour un diagnostic précis et un plan de traitement approprié.")                     
  
        else:
          diab_diagnosis = 'The person is not diabetic'
          st.write('- Based on your inputs, you appear to be at a lower risk for developing diabetes. However, it is always a good idea to maintain a healthy lifestyle to reduce your risk. Try to incorporate more fruits and vegetables into your diet, limit your intake of sugary foods and drinks, and increase your physical activity. It is also recommended that you schedule regular check-ups with your doctor to monitor your health.')
        
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        age=float(age)
        sex=float(sex)
        cp=float(cp)
        trestbps=float(trestbps)
        chol=float(chol)
        fbs=float(fbs)
        restecg=float(restecg)
        thalach=float(thalach)
        exang=float(exang)
        oldpeak=float(oldpeak)
        slope=float(slope)
        ca=float(ca)
        thal=float(thal)
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
            if age > 60:
                print("You should consider regular check-ups and follow a heart-healthy lifestyle.")
            
            # Resting Blood Pressure
            if trestbps > 140:
                print("It is recommended to monitor your blood pressure regularly and consult a doctor.")
            
            # Resting Electrocardiographic results
            if restecg == 1:
                print("You may need further cardiac tests to evaluate your heart's electrical activity.")
            
            # ST depression induced by exercise
            if oldpeak > 2:
                print("You should consult a doctor for further evaluation of possible heart disease.")
            
            # thal
            if thal == 0:
                print("Your thalassemia test result is normal.")
            elif thal == 1:
                print("Your thalassemia test indicates a fixed defect. Consult a doctor for further evaluation.")
            elif thal == 2:
                print("Your thalassemia test indicates a reversible defect. Consult a doctor for further evaluation.")
            
            # Sex
            if sex == 0:
                print("Being female reduces the risk of heart disease. However, it is still important to maintain a healthy lifestyle.")
            
            # Serum Cholestoral in mg/dl
            if chol > 240:
                print("Your cholesterol level is high. Adopt a heart-healthy diet and lifestyle changes.")
            
            # Maximum Heart Rate achieved
            if thalach < 100 or thalach > 180:
                print("Your maximum heart rate achieved is outside the normal range. Consult a doctor for further evaluation.")
            
            # Slope of the peak exercise ST segment
            if slope == 2:
                print("The slope of your peak exercise ST segment indicates a high risk of heart disease. Consult a doctor.")
            
            # Chest Pain types
            if cp == 1:
                print("Your chest pain type suggests typical angina. Consult a doctor for further evaluation.")
            elif cp == 2:
                print("Your chest pain type suggests atypical angina. Consult a doctor for further evaluation.")
            elif cp == 3:
                print("Your chest pain type suggests non-anginal pain. Monitor your symptoms and consult a doctor if necessary.")
            
            # Fasting Blood Sugar > 120 mg/dl
            if fbs == 1:
                print("Your fasting blood sugar level is above normal. Monitor your blood sugar and adopt a healthy lifestyle.")
            
            # Exercise Induced Angina
            if exang == 1:
                print("You have exercise-induced angina. Consult a doctor for further evaluation and appropriate treatment.")
            
        # Major vessels colored by flourosopy
            if ca == 0:
                print("The number of major vessels colored by flourosopy indicates no significant heart disease.")
            elif ca > 0:
                print("The number of major vessels colored by flourosopy indicates the presence of heart disease. Consult a doctor.")

            if int(chol) < 30:
                st.write('Your Cholestoral level is low. You should consult with a doctor to determine if you are at risk for developing Parkinson\'s disease.')
            else:
                st.write('Based on your inputs, you appear to be at a lower risk for developing Parkinson\'s disease. However, it is always a good idea to maintain a healthy lifestyle to reduce your risk.')    

        else:
          heart_diagnosis = 'The person does not have any heart disease'
          st.write('- Based on your inputs, you appear to be at a lower risk for developing heart disease. However, it is still important to maintain a healthy lifestyle to reduce your risk of developing heart disease.')

    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        fo = float(fo)
        fhi = float(fhi)
        PPQ = float(PPQ)
        APQ5 = float(APQ5)
        RPDE = float(RPDE)
        PPE = float(PPE)
        flo = float(flo)
        DDP = float(DDP)
        APQ3 = float(APQ3)
        DFA = float(DFA)
        Jitter_percent = float(Jitter_percent)
        Shimmer = float(Shimmer)
        Shimmer_dB = float(Shimmer_dB)
        spread1 = float(spread1)
        Jitter_Abs = float(Jitter_Abs)
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
            if fo < 100:
                st.write("- Augmentez l'intensité de votre voix lors de la parole.")
            if fhi > 300:
                st.write("- Essayez de parler plus doucement pour éviter les tensions vocales.")
                
            if PPQ > 20:
                st.write("- Pratiquez des exercices de respiration pour améliorer le contrôle de votre voix.")
                
            if APQ5 > 10:
                st.write("- Travaillez avec un orthophoniste pour améliorer la stabilité de votre voix.")
                
            if RPDE > 10:
                st.write("- Pratiquez des exercices de modulation de la voix pour améliorer sa clarté.")
                
            if PPE > 48:
                st.write("- Travaillez sur des exercices d'articulation pour améliorer la précision de votre parole.")
                
            if flo < 80:
                st.write("- Consultez un professionnel de la voix pour évaluer votre santé vocale.")
                
            if DDP > 34:
                st.write("- Pratiquez des exercices de relaxation pour réduire les tensions vocales.")
                
            if APQ3 > 25:
                st.write("- Travaillez sur des exercices de vocalisation pour améliorer la qualité de votre voix.")
                
            if DFA > 58:
                st.write("- Consultez un spécialiste de la voix pour obtenir des exercices personnalisés.")
                
            if Jitter_percent > 23:
                st.write("- Essayez des exercices d'échauffement vocal pour améliorer la stabilité de votre voix.")
                
            if Shimmer > 12:
                st.write("- Travaillez avec un orthophoniste pour réduire l'irrégularité de votre voix.")
                
            if Shimmer_dB > 15:
                st.write("- Pratiquez des exercices de respiration pour améliorer le contrôle de votre voix.")
                
            if spread1 > 6:
                st.write("- Travaillez sur des exercices de modulation de la voix pour éviter les tensions vocales.")
                
            if Jitter_Abs > 63:
                st.write("- Consultez un professionnel de la voix pour évaluer votre santé vocale.")
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
















