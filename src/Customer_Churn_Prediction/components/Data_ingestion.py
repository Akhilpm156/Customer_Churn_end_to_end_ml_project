import os
import urllib.request as request
import zipfile
from pathlib import Path
from Customer_Churn_Prediction import logger
from Customer_Churn_Prediction.utils.common import get_size
from Customer_Churn_Prediction.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def Download_file(self):
        if not os.path.exists(self.config.data_path):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename = self.config.data_path            
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.data_path))}")

    def Extract_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.data_path,"r") as zip_ref:
            zip_ref.extractall(unzip_path)