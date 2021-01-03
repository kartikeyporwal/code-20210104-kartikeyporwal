import json

import numpy as np
import pandas as pd


def calc_bmi(mass, height):
    """Calculates BMI from specified height and mass

    BMI(kg/m2) = mass(kg) / height(m)2

    Arguments:
        mass {float} -- mass of the person in KG
        height {float} -- height of the person in meters

    Returns:
        bmi {float} -- Body Mass Index of the person from specified mass and height
    """
    bmi = mass/(height**2)
    bmi = round(bmi, 1)  # rounding off to 1 digit after decimal
    return bmi


def process_person_json(json_data):
    """Calculates BMI of json data and adds `BMI Category` and `Health Risk` based on BMI value

    Arguments:
        json_data {str} -- json data to be processed

    Returns
        result {str} -- processed json data with `BMI`, `BMI Category` and `Health Risk` added 
        along with category-wise person count
    """
    # pre-specifying datatype to save some memory
    df = pd.read_json(json_data,
                      dtype={
                          "Gender": "category",
                          "HeightCm": np.float,
                          "WeightKg": np.float,
                      })

    df["BMI"] = df[["WeightKg", "HeightCm"]].apply(
        lambda x: calc_bmi(mass=x[0], height=x[1]/100), axis=1)

    # performing vectorize operations for efficient calculations
    bmi_conditions = [
        (df["BMI"] <= 18.4),
        (18.5 <= df["BMI"]) & (df["BMI"] <= 24.9),
        (25 <= df["BMI"]) & (df["BMI"] <= 29.9),
        (30 <= df["BMI"]) & (df["BMI"] <= 34.9),
        (35 <= df["BMI"]) & (df["BMI"] <= 39.9),
        (40 <= df["BMI"]),
    ]

    bmi_categories = [
        "Underweight",
        "Normal weight",
        "Overweight",
        "Moderately obese",
        "Severely obese",
        "Very severely obese",
    ]

    health_risk = [
        "Malnutrition risk",
        "Low risk",
        "Enhanced risk",
        "Medium risk",
        "High risk",
        "Very high risk",
    ]

    df["BMICategory"] = np.select(bmi_conditions, bmi_categories, None)
    df["HealthRisk"] = np.select(bmi_conditions, health_risk, None)

    # calculating person count of each bmi category
    person_count = np.sum(bmi_conditions, axis=1, dtype=np.int)
    nos_people = {
        f"{key} count": int(value)
        for key, value in zip(bmi_categories, person_count)
    }

    result = json.dumps({
        "updatedJson": df.to_dict("records"),
        **nos_people
    })

    return result


if __name__ == "__main__":

    # json string
    json_data = json.dumps([{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                            {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}])
    res = process_person_json(json_data=json_data)
    print(res)

