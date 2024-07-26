import argparse
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Load data
data = pd.read_csv("data/diabetes.csv")

def main(random_state, max_iter):

    X = data.drop('Outcome',axis=1)
    y = data['Outcome']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression(random_state=random_state, max_iter=max_iter)
    model.fit(X_train, y_train)
        
    # Predict and evaluate
    predictions = model.predict(X_test)
    
    accuracy = metrics.accuracy_score(y_test, predictions)
    precision = metrics.precision_score(y_test, predictions)
    recall = metrics.recall_score(y_test, predictions)

    # Log parameters, metrics, and model
    mlflow.log_param("random_state", random_state)
    mlflow.log_param("max_iter", max_iter)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)

    # Use when you dont want to register your model
    # mlflow.sklearn.log_model(model, "model")

    # Register the model
    mlflow.sklearn.log_model(model, "model", registered_model_name="model_diabetes_prediction")

    print("Training Done!!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--random_state", type=int, default=0)
    parser.add_argument("--max_iter", type=int, default=100)
    args = parser.parse_args()
    
    # Start a new MLflow run
    with mlflow.start_run():
        main(args.random_state, args.max_iter)