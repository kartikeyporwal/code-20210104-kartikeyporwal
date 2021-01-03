# BMI Calculator

**Formula:** `BMI(kg/m2) = mass(kg) / height(m)2`

Table 1 - BMI Category and the Health Risk.
|BMI Category        |BMI Range (kg/m2) |Health risk
| ------------------ |:----------------:| ---------------:|
|Underweight         |18.4 and below    |Malnutrition risk
|Normal weight       |18.5 - 24.9       |Low risk
|Overweight          |25 - 29.9         |Enhanced risk
|Moderately obese    |30 - 34.9         |Medium risk
|Severely obese      |35 - 39.9         |High risk
|Very severely obese |40 and above      |Very high risk  


**Tasks:**  
- Reads Json data
- Calculates `BMI` from `mass` and `height`
- Maps `BMI Category` and `Health Risk` based on the BMI
- Updates Json with `BMI`, `BMICategory`, `HealthRisk`
- Calculates `person count` based on the `BMICategory` and maps with respective `BMICategory` as new key of the resulting json

**To install the project:**  
    `python -m venv bmi_env`  
    `python -m pip install -r requirements.txt`  

**To Run unit test:**  
    `python -m unittest`
    OR  
    `python test.py`  

**To Run script:**  
    `python bmi.py`
