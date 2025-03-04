import os
import pandas as pd
from Customer_Churn_Prediction import logger
from Customer_Churn_Prediction.entity.config_entity import ModelTrainerConfig
import joblib
from sklearn.tree import DecisionTreeClassifier


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        dtree = DecisionTreeClassifier(criterion = self.config.criterion, max_depth=self.config.max_depth, random_state=42)
        dtree.fit(train_x, train_y)

        joblib.dump(dtree, os.path.join(self.config.root_dir, self.config.model_name))

        # Now move the model to the `model` directory outside the `src` folder
        final_model_path = os.path.join("model", "model.joblib")  # Save model to the 'model' folder

        # Create directories if they do not exist
        if not os.path.exists(os.path.dirname(final_model_path)):
            os.makedirs(os.path.dirname(final_model_path))
            print(f"✅ Folder Created: {os.path.dirname(final_model_path)}")

        # Move the model to final destination
        joblib.dump(dtree, final_model_path)
        print(f"✅ Model Moved to: {final_model_path}")