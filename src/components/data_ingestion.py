import os
import sys
from src.logger import logging
from src.exception import CustomException

import pandas
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#for 
@dataclass # decorater , makes it easier to define variables
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")#all the data ingestion ouput will be saved in this path
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("entered data ingestion method")#to read code from a database say mongodb or sql client
        try:
            df=pd.read_csv('notebook\StudentsPerformance.csv')
            logging.info("read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Test Train split initiated")
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

            
            

            


