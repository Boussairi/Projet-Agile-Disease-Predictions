import unittest
from unittest.mock import patch
from io import StringIO
from mdps_public import *


class TestDiseasePrediction(unittest.TestCase):

    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    def test_diabetes_prediction(self):
        input_values = [1, 85, 66, 29, 0, 26.6, 0.351, 31]
        expected_output = 'The person is not diabetic'
       # with patch('builtins.input', side_effect=input_values), patch('sys.stdout', new=StringIO()) as fake_out:
        #    diabetes_prediction()
            self.assertEqual(fake_out.getvalue().strip(), expected_output)
        result = diabetes_model.predict([input_values])                          
        self.assertEqual(result, expected_output)
            
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
