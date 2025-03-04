from Customer_Churn_Prediction.config.configuration import ConfigurationManager
from Customer_Churn_Prediction.components.Data_ingestion import DataIngestion
from Customer_Churn_Prediction import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.Download_file()
        data_ingestion.Extract_file()
    except Exception as e:
        raise e