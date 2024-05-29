import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(df, target):
    # Split data into features and target
    X = df.drop(target, axis=1)
    y = df[target]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
