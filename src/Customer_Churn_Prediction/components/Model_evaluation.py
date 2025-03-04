import os
import pandas as pd
from Customer_Churn_Prediction import logger
from Customer_Churn_Prediction.utils.common import save_json
from Customer_Churn_Prediction.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,actual, pred):
        #clsreport = classification_report(actual, pred)
        #cm = confusion_matrix(actual, pred)
        accuracy = accuracy_score(actual, pred)
        # return clsreport, cm, accuracy
        return accuracy
    


    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        y_pred = model.predict(test_x)

        #(clsreport,cm,accuracy) = self.eval_metrics(test_y, y_pred)
        accuracy = self.eval_metrics(test_y, y_pred)

        # Saving metrics as local
        scores = {"accuracy_score": accuracy}
        save_json(path=Path(self.config.metric_file_name), data=scores)