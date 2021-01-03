import json
import unittest

from bmi import process_person_json


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can process json data as required
        """
        json_data = json.dumps([{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                                {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                                {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                                {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                                {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                                {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}])

        expected_result = json.dumps({
            "updatedJson": [
                {"Gender": "Male", "HeightCm": 171.0, "WeightKg": 96.0, "BMI": 32.8,
                    "BMICategory": "Moderately obese", "HealthRisk": "Medium risk"},
                {"Gender": "Male", "HeightCm": 161.0, "WeightKg": 85.0, "BMI": 32.8,
                    "BMICategory": "Moderately obese", "HealthRisk": "Medium risk"},
                {"Gender": "Male", "HeightCm": 180.0, "WeightKg": 77.0, "BMI": 23.8,
                    "BMICategory": "Normal weight", "HealthRisk": "Low risk"},
                {"Gender": "Female", "HeightCm": 166.0, "WeightKg": 62.0, "BMI": 22.5,
                    "BMICategory": "Normal weight", "HealthRisk": "Low risk"},
                {"Gender": "Female", "HeightCm": 150.0, "WeightKg": 70.0, "BMI": 31.1,
                    "BMICategory": "Moderately obese", "HealthRisk": "Medium risk"},
                {"Gender": "Female", "HeightCm": 167.0, "WeightKg": 82.0, "BMI": 29.4,
                    "BMICategory": "Overweight", "HealthRisk": "Enhanced risk"}
            ],
            "Underweight count": 0,
            "Normal weight count": 2,
            "Overweight count": 1,
            "Moderately obese count": 3,
            "Severely obese count": 0,
            "Very severely obese count": 0
        })

        result = process_person_json(json_data)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
