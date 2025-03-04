from Customer_Churn_Prediction.config.configuration import ConfigurationManager
from Customer_Churn_Prediction.components.Data_Transformation import DataTransformation
from Customer_Churn_Prediction import logger


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    try:
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.preprocessing_data()
    except Exception as e:
        raise e