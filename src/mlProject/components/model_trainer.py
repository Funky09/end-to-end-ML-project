from sklearn.linear_model import ElasticNet
import joblib
import pandas as pd
from mlProject.config.configuration import ModelTrainerConfig
import os


class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig) :
        self.config = config

    def train_model(self):
        train = pd.read_csv(self.config.train_data_path)
        test = pd.read_csv(self.config.test_data_path)

        train_x = train.drop([self.config.target_col],axis=1)
        test_x = test.drop([self.config.target_col],axis=1)

        train_y = train[[self.config.target_col]]
        test_y = test[[self.config.target_col]]

        lr = ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio,random_state=42)
        lr.fit(train_x,train_y)

        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))