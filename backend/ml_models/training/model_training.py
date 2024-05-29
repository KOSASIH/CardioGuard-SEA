import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from ml_models.preprocessing.data_preparation import prepare_data

def train_model(X_train, y_train):
    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    return model

def train_model_with_cross_validation(X_train, y_train, cv=5):
    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Perform cross-validation
    scores = []
    for train_index, val_index in cv.split(X_train):
        X_train_fold = X_train[train_index]
        y_train_fold = y_train[train_index]
        X_val_fold = X_train[val_index]
        y_val_fold = y_train[val_index]

        # Train the model on the current fold
        model.fit(X_train_fold, y_train_fold)

        # Evaluate the model on the current fold
        y_pred = model.predict(X_val_fold)
        scores.append(accuracy_score(y_val_fold, y_pred))

    # Calculate the average score
    avg_score = np.mean(scores)

    return model, avg_score

def main():
    # Load the data
    X, y = prepare_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    main()
