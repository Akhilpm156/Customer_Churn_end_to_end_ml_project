from Customer_Churn_Prediction.config.configuration import ConfigurationManager
from Customer_Churn_Prediction.components.Model_evaluation import ModelEvaluation
from Customer_Churn_Prediction import logger


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    try:
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()
    except Exception as e:
        raise e