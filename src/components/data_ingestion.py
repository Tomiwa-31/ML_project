import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")#defining the path that will stores the training data
    test_data_path: str=os.path.join('artifacts',"test.csv")#creates a folder based on the current working directory
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(r'C:\ML_project\src\notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            # Ensure the directory exists
            dir_path = os.path.dirname(self.ingestion_config.train_data_path)
            print(f"Attempting to create directory: {dir_path}")
            
            if dir_path:  # Ensure the path is not empty
                os.makedirs(dir_path, exist_ok=True)
                print(f"Directory created successfully: {dir_path}")
            else:
                print("Error: Directory path is empty!")
                return

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    #obj.initiate_data_ingestion()

    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    #modeltrainer=ModelTrainer()
    #print(modeltrainer.initiate_model_trainer(train_arr,test_arr))


