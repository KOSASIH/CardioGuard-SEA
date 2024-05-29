import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def evaluate_model(model, X_test, y_test):
    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Calculate classification report
    report = classification_report(y_test, y_pred)

    # Calculate confusion matrix
    matrix = confusion_matrix(y_test, y_pred)

    return accuracy, report, matrix

def main():
    # Load the data
    X, y = prepare_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    accuracy, report, matrix = evaluate_model(model, X_test, y_test)
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(report)
    print("Confusion Matrix:")
    print(matrix)

if __name__ == "__main__":
    main()
