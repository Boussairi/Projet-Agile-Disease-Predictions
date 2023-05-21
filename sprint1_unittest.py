import unittest
from Diabetes_Prediction_web_app import diabetes_prediction

class TestDiabetesPrediction(unittest.TestCase):

    def test_diabetes_prediction(self):
        # Test case 1: Non-diabetic person
        input_data = [6,148,72,35,0,33.6,0.627,50]
        expected_output = 'The person is diabetic'
        self.assertEqual(diabetes_prediction(input_data), expected_output)

        # Test case 2: Diabetic person
        input_data = [1,85,66,29,0,26.6,0.351,31]
        expected_output = 'The person is not diabetic'
        self.assertEqual(diabetes_prediction(input_data), expected_output)

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
