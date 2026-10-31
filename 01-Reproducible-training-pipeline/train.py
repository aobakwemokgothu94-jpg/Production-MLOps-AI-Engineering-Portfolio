This script implements a scikit-learn training pipeline integrated with MLflow for automated metric tracking and artifact logging

import mlflow
import mlflow.sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

def run_training():
    # Load and split dataset (DataCamp Supervised Learning practice)
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    # Start MLflow experiment tracking run
    with mlflow.start_run(run_name="rf_reproducible_run"):
        n_estimators = 120
        max_depth = 6

        model = RandomForestClassifier(
            n_estimators=n_estimators, 
            max_depth=max_depth, 
            random_state=42
        )
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        # Log parameters and metrics
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)

        # Log model artifact
        mlflow.sklearn.log_model(model, "random_forest_model")
        print(f"[SUCCESS] Training complete. Accuracy: {acc:.4f}, F1-Score: {f1:.4f}")

if __name__ == "__main__":
    run_training()
