import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

def select_model(X_train, y_train):
    # Define the model and hyperparameters
    model = RandomForestClassifier()
    params = {
        'n_estimators': [100, 200, 300],
        'ax_depth': [None, 5, 10]
    }

    # Perform grid search
    grid = GridSearchCV(model, params, cv=5, scoring='accuracy')
    grid.fit(X_train, y_train)

    # Get the best model and hyperparameters
    best_model = grid.best_estimator_
    best_params = grid.best_params_

    return best_model, best_params

def main():
    # Load the data
    X, y = prepare_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Select the model
    best_model, best_params = select_model(X_train, y_train)
    print("Best Model:", best_model)
    print("Best Hyperparameters:", best_params)

if __name__ == "__main__":
    main()
