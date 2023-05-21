from unittest.mock import patch
from io import StringIO

import unittest
from mdps_public import *

class TestMyScript(unittest.TestCase):

    def test_diabetes_prediction(self):
        # Créez un objet du formulaire de saisie de données
        form_data = {
            'Number of Pregnancies': '6',
            'Glucose Level': '148',
            'Blood Pressure value': '72',
            'Skin Thickness value': '35',
            'Insulin Level': '0',
            'BMI value': '33.6',
            'Diabetes Pedigree Function value': '0.627',
            'Age of the Person': '50'
        }

        # Appelez la fonction de prédiction pour le diabète avec les données du formulaire
        result = diabetes_prediction(form_data)

        # Vérifiez si le résultat est correct
        self.assertEqual(result, 'The person is diabetic')

    def test_heart_disease_prediction(self):
        # Créez un objet du formulaire de saisie de données
        form_data = {
            'Age': '63',
            'Sex': '1',
            'Chest Pain types': '3',
            'Resting Blood Pressure': '145',
            'Serum Cholestoral in mg/dl': '233',
            'Fasting Blood Sugar > 120 mg/dl': '1',
            'Resting Electrocardiographic results': '0',
            'Maximum Heart Rate achieved': '150',
            'Exercise Induced Angina': '0',
            'ST depression induced by exercise': '2.3',
            'Slope of the peak exercise ST segment': '0',
            'Major vessels colored by flourosopy': '0',
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect': '1'
        }

        # Appelez la fonction de prédiction pour les maladies cardiaques avec les données du formulaire
        result = heart_disease_prediction(form_data)

        # Vérifiez si le résultat est correct
        self.assertEqual(result, 'The person is having heart disease')

    def test_parkinsons_prediction(self):
        # Créez un objet du formulaire de saisie de données
        form_data = {
            'MDVP:Fo(Hz)': '119.992',
            'MDVP:Fhi(Hz)': '157.302',
            'MDVP:Flo(Hz)': '74.997',
            'MDVP:Jitter(%)': '0.00784',
            'MDVP:Jitter(Abs)': '7e-05',
            'MDVP:RAP': '0.0037',
            'MDVP:PPQ': '0.00554',
            'Jitter:DDP': '0.01109',
            'MDVP:Shimmer': '0.04374',
            'MDVP:Shimmer(dB)': '0.426',
            'Shimmer:APQ3': '0.02182',
            'Shimmer:APQ5': '0.0313',
            'MDVP:APQ': '0.02971',
            'Shimmer:DDA': '0.06545',
            'NHR': '0.02211',
            'HNR': '21.033',
            'RPDE': '0.414783',
            'RPDE': '0.414783',
            'DFA': '0.815285',
            'spread1': '-4.81303',
            'spread2': '0.266482',
            'D2': '2.301442',
            'PPE': '0.284654'            }
           # Appelez la fonction de prédiction pour les maladies cardiaques avec les données du formulaire
        result = parkinsons_prediction(form_data)

        # Vérifiez si le résultat est correct
        self.assertEqual(result, 'The person has Parkinson\'s disease')
if name == 'main':
    unittest.main()
#class TestDiseasePrediction(unittest.TestCase):  
# Diabetes Prediction Page
#if (selected == 'Diabetes Prediction'):
 #   def test_diabetes_prediction(self):
  #      input_values = [1, 85, 66, 29, 0, 26.6, 0.351, 31]
   #     expected_output = 'The person is not diabetic'
       # with patch('builtins.input', side_effect=input_values), patch('sys.stdout', new=StringIO()) as fake_out:
        #    diabetes_prediction()
            self.assertEqual(fake_out.getvalue().strip(), expected_output)
    #    result = diabetes_model.predict([input_values])                          
     #   self.assertEqual(result, expected_output)
            
#if (selected == 'Heart Disease Prediction'):
 #   def test_heart_disease_prediction(self):
  #      input_values = [20, 1, 0, 5, 21, 0, 0, 6, 1, 0.9, 1, 2, 2]
   #     expected_output = 'The person does not have any heart disease'
    #    with patch('builtins.input', side_effect=input_values), patch('sys.stdout', new=StringIO()) as fake_out:
     #       heart_disease_prediction()
      #      self.assertEqual(fake_out.getvalue().strip(), expected_output)

#    def test_parkinsons_prediction(self):
 #       input_values = ['150', '200', '100', '0.5', '0.02', '0.05', '0.08', '0.06', '0.04', '0.06', '0.04', '0.07', '0.05', '0.06', '0.05', '0.02', '0.08', '0.07', '0.04', '0.05', '0.08', '0.06']
  #      expected_output = "The person doesn't have Parkinson's disease"
   #     with patch('builtins.input', side_effect=input_values), patch('sys.stdout', new=StringIO()) as fake_out:
    #        parkinsons_prediction()
     #       self.assertEqual(fake_out.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
