import os
import pandas as pd
from Customer_Churn_Prediction import logger
from Customer_Churn_Prediction.utils.common import save_json
from Customer_Churn_Prediction.entity.config_entity import ModelEvaluationConfig
import joblib
from pathlib import Path
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import mlflow
from urllib.parse import urlparse

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def load_model(self, path: Path):
        self.model = joblib.load(path)
        return self.model



    def eval_metrics(self):
        test_data = pd.read_csv(self.config.test_data_path)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        self.model=self.load_model(self.config.model_path)
        pred = self.model.predict(test_x)
        clsreport = classification_report(test_y, pred)
        cm = confusion_matrix(test_y, pred)
        accuracy = accuracy_score(test_y, pred)

        self.accuracy = accuracy
        self.clsreport = clsreport
        self.cm = cm

        return clsreport, cm, accuracy
        

    def save_results(self):
        # Saving metrics as local
        if not hasattr(self, 'accuracy'):
            raise ValueError("Call eval_metrics() before saving results.")

        scores = {"accuracy_score": self.accuracy}
        save_json(path=Path(self.config.metric_file_name), data=scores)



    def log_into_mlflow(self):

        if not hasattr(self, 'accuracy'):
            raise ValueError("Call eval_metrics() before logging to MLflow.")

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_registry_uri(self.config.mlflow_uri)
        mlflow.set_experiment("Customer_Churn_Experiment")

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"accuracy": self.accuracy}
            )

            with open("artifacts/model_evaluation/classification_report.txt", "w") as f:
                f.write(self.clsreport)
            with open("artifacts/model_evaluation/confusion_matrix.txt", "w") as f:
                f.write(str(self.cm))

            mlflow.log_artifact("artifacts/model_evaluation/classification_report.txt")
            mlflow.log_artifact("artifacts/model_evaluation/confusion_matrix.txt")

            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow

                mlflow.sklearn.log_model(self.model, "model", registered_model_name="DecisionTreeClassifier")
            else:
                mlflow.sklearn.log_model(self.model, "model")