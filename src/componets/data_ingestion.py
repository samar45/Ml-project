import os
import sys
from src.exception import CostumException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts',"train.csv")
    test_data_path : str=os.path.join('artifacts',"test.csv")
    raw_data_path : str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def inicate_data_ingestion(self):
        logging.info("Enterd the data ingestion methord or component")
        try:
            df =pd.read_csv("notebook\data\stud.csv")
            logging.info ('read the dataset as data frame')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path ,index=False,header=True)
            
            logging.info("Train test slpit inicated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path ,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path ,index=False,header=True)
        
            logging.info("ingestion of the data is completed")

            return (
                self.ingestion_config.test_data_path,
                self.ingestion_config.test_data_path,

            )
        
        except Exception as E:
            raise CostumException (E,sys)
        

if __name__== "__main__":
    obj = DataIngestion()
    obj.inicate_data_ingestion()

    