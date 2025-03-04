import os
import pandas as pd
from Customer_Churn_Prediction import logger
from Customer_Churn_Prediction.entity.config_entity import DataTransformationConfig
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def preprocessing_data(self):
        data = pd.read_csv(self.config.data_path)
        # drop columns
        data.drop(['RowNumber','CustomerId','Surname'],axis = 1,inplace=True)

        # seperate catgory and numrical columns
        df_cat = data.select_dtypes(include='object')
        df_num = data.select_dtypes(exclude='object')

        # One hot encoding
        df_cat = pd.get_dummies(df_cat, columns=['Geography', 'Gender', 'Card Type'], drop_first=True,dtype='int')

        # final dataframe
        dfp = pd.concat([df_cat,df_num],axis=1)

        # Handling imbalnce in the data
        X = dfp.drop(columns=['Exited'])
        y = dfp['Exited']
        smote = SMOTE(sampling_strategy=0.5, random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X, y)
        resampled_data = pd.concat([X_resampled,y_resampled],axis=1)

        # Train Test split
        train, test = train_test_split(resampled_data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        #print(train.shape)
        #print(test.shape)