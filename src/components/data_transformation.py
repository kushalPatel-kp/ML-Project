import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.exception import CutsomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numeric_feature = ['reading_score',	'writing_score']
            cat_feature = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            num_pipeline = Pipeline(
                steps=[
                ("impute", SimpleImputer(strategy='median')),
                ("scalar", StandardScaler())
            ])

            cat_pipeline=Pipeline(
                steps=[
                    ("impute", SimpleImputer(strategy='most_frequent')),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scalar", StandardScaler(with_mean=False))
                ]
            )

            logging.info("Categorical columns encoded")

            logging.info("numerical columns standard scalling complected")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numeric_feature),
                    ("cat_pipeline", cat_pipeline, cat_feature)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CutsomException(e, sys)
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            train_df.columns = train_df.columns.str.strip()
            test_df.columns = test_df.columns.str.strip()

            logging.info("Readed the Train and Test data")

            preprocessiong_obj = self.get_data_transformer_object()

            target_column_name = "math_score"


            input_feature_train_df=train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df=train_df[target_column_name]


            input_feature_test_df=test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("Applying the preprocessing object on training and test dataframe")

            inpt_feature_train_arr=preprocessiong_obj.fit_transform(input_feature_train_df)
            print(inpt_feature_train_arr)
            inpt_feature_test_arr=preprocessiong_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                inpt_feature_train_arr, np.array(target_feature_train_df)
            ]
            print(pd.DataFrame(train_arr))
            test_arr = np.c_[
                inpt_feature_test_arr, np.array(target_feature_test_df)
            ]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessiong_obj
            )

            return(train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path)

        except Exception as e:
            raise CutsomException(e,sys)