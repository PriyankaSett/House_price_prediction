import os 
import sys 
import pandas as pd 
import numpy as np
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import StandardScaler, RobustScaler, FunctionTransformer 

from src.exception import CustomException
from src.logger import logging 
from src.utils import save_object




@dataclass
class DataTransformationConfig: 
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')



class DataTransformation: 
    def __init__(self): 
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation(self):
        """
        This function defines the steps to transform the given data. Like, 
        the numerical/categorical columns are assigned. Then depending on the 
        feature pipelines are created to transform the data. This function will 
        return the preprocessor object.   
        """ 
        
        try : 
            logging.info('Data transformation initiated')

            numerical_columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 
                                 'NOX', 'RM', 'AGE', 'DIS',
                                 'PTRATIO', 'B', 'LSTAT']
            
            
            
            logging.info('Pipline initiated')


            # numerical pipeline
            num_pipeline = Pipeline(
                steps=[('imputer', SimpleImputer(strategy='median')), 
                    ('scaler', RobustScaler()) # this is used as the data have outliers
                ]
            )


            # preprocessor 
            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_columns)
            ])
            
            return preprocessor

            logging.info('Pipeline Completed')


        except Exception as e: 
            logging.info('Error in Data Transformation')
            raise CustomException(e, sys)
        

    def initiate_data_transformation(self, train_path, test_path): 
        """
        Given the train and test data this function will perform the transformations 
        defined in the 'get_data_transformation.' After transforming the input data, 
        this function will return the transformed train and test data and the preprocessor
        pickle file which can reused as required. 
        
        """

        try: 
            # reading the train and test data : 
            train_df = pd.read_csv(train_path)
            test_df  = pd.read_csv(test_path)

            logging.info('Reading of train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')


            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation() 


            target_col_name = 'target'
            dropped_col_names = ['target', 'Unnamed: 0']
            # TAX and RAD are dropped as they have high VIF. 

            input_feature_train_df = train_df.drop(columns = dropped_col_names,axis=1)
            target_feature_train_df = train_df[target_col_name]

            input_feature_test_df = test_df.drop(columns=dropped_col_names,axis=1)
            target_feature_test_df = test_df[target_col_name]
            

            ## Transformation using preprocessor obj
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            
            logging.info("Applying preprocessing object on training and testing datasets.")
            

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(

                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj

            )

            logging.info('Preprocessor pickle file saved')
    
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )



        except Exception as e : 
            logging.info('Error occured in initiate data transformation.')
            raise CustomException(e, sys)
