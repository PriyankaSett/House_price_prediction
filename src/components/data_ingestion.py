import os 
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# Initialize the data ingestion configuration 

@dataclass
class DataIngestionconfig: 
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')


# create a class for data ingestion 

class DataIngestion:
    def __init__(self): 
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self): 
        logging.info('Data Ingestion method starts')
        try :
            df=pd.read_csv(os.path.join('notebooks/data', 'boston_data.csv'))
            
            logging.info('Dataset read as pandas dataframe.')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info('Raw data set saved.')

            logging.info('Train test split.')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state = 42)
            logging.info('Train test split successful.')

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info('Ingestion of data is completed.')

            return(
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )


        except Exception as e: 
            logging.info('Exception occured at Data Ingestion stage') 
            raise CustomException(e,sys) 

# run data ingestion just for testing
"""
if __name__ == '__main__': 
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
"""    






