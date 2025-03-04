from Customer_Churn_Prediction.config.configuration import ConfigurationManager
from Customer_Churn_Prediction.components.Model_training import ModelTrainer
from Customer_Churn_Prediction import logger


STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    try:
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
    except Exception as e:
        raise e