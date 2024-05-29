import pandas as pd
import numpy as np

def clean_data(df):
    # Remove rows with missing values
    df = df.dropna()

    # Handle outliers
    df['blood_pressure'] = np.where(df['blood_pressure'] > 220, np.nan, df['blood_pressure'])
    df['blood_pressure'] = np.where(df['blood_pressure'] < 50, np.nan, df['blood_pressure'])

    # Handle inconsistent data types
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['gender'] = df['gender'].astype('category')
    df['smoker'] = df['smoker'].astype('category')

    return df
