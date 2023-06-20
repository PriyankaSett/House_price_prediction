import os 
import sys 
import pandas as pd 
import numpy as np
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging 
from src.utils import save_object, evaluate_model

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
#from sklearn.neighbors import KNeighborsRegressor
#from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


@dataclass
class ModelTrainerConfig : 
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:

    def __init__(self) : 
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_training(self, train_array, test_array) : 
        """
        Given the training data, model training takes place. 
        """     

        try : 
            
            logging.info('Splitting dependent and independent variable from train and test data.')

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1], train_array[:, -1], 
                test_array[:, :-1], test_array[:, -1]
            )

            models={
                    'LinearRegression':LinearRegression(),
                    'Lasso':Lasso(),
                    'Ridge':Ridge(),
                    'Elasticnet':ElasticNet(), 
                    'DecisionTree':DecisionTreeRegressor(), 
                    'RandomForest':RandomForestRegressor()
                    }
            
            model_report:dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print('\n-----------------------------------------')

            logging.info(f'Model Report : {model_report}')

            # to get the best score from model report dictionary

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model, Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model, Model Name : {best_model_name} , R2 Score : {best_model_score}')


            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
          

        except Exception as e : 
            logging.info('Error occured in initiate model training.')
            raise CustomException(e, sys)
