import unittest
from unittest.mock import patch
from io import StringIO
from mdps_public import *

class TestDiseasePrediction(unittest.TestCase):

    def test_diabetes_prediction(self):
        input_values = ['1','85','66','29','0','26.6','0.351','31']
        output = StringIO()
        with patch('builtins.input', side_effect=input_values), patch('sys.stdout', output):
            diabetes_prediction()
        self.assertEqual(output.getvalue().strip(), 'The person is not diabetic')

    def test_heart_disease_prediction(self):
        input_values = ['20','1',0,'5','21','0','0','6','1','0.9','1','2','2']
        output = StringIO()
        with patch('builtins.input', side_effect=input_values), patch('sys.stdout', output):
            heart_disease_prediction()
        self.assertEqual(output.getvalue().strip(), 'The person does not have any heart disease')

 #   def test_parkinsons_prediction(self):
  #      input_values = ['150', '200', '100', '0.5', '0.02', '0.05', '0.08', '0.06', '0.04', '0.06', '0.04', '0.07', '0.05', '0.06', '0.05', '0.02', '0.08', '0.07', '0.04', '0.05', '0.08', '0.06']
   #     output = StringIO()
    #    with patch('builtins.input', side_effect=input_values), patch('sys.stdout', output):
     #       parkinsons_prediction()
      #  self.assertEqual(output.getvalue().strip(), "The person doesn't have Parkinson's disease")

if __name__ == '__main__':
    unittest.main()
