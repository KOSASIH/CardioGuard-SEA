import pandas as pd

def create_new_features(df):
    # Create a new feature for age categories
    df['age_category'] = pd.cut(df['age'], bins=[0, 20, 40, 60, 100], labels=['0-20', '21-40', '41-60', '61-100'])

    # Create a new feature for BMI categories
    df['bmi_category'] = pd.cut(df['bmi'], bins=[0, 18.5, 25, 30, 100], labels=['Underweight', 'Normal weight', 'Overweight', 'Obese'])

    return df
