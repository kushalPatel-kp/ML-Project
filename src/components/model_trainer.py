import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from src.exception import CutsomException
from src.logger import logging
from src.utils import save_object, evalute_model

@dataclass
class ModelTrainerConfig:
    trainde_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("Spliting, training and test input data")
            X_train, y_train, X_test, y_test=(train_arr[:,:-1], train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1])

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decesion Tree": DecisionTreeRegressor(),
                "LinearRegression": LinearRegression(),
                "Adaboost": AdaBoostRegressor(),
                "GradientBoosting": GradientBoostingRegressor(),
                "Knn": KNeighborsRegressor(),
                "SVM": SVR()
            }

            model_report: dict=evalute_model(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models)
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            
            if best_model_score < 0.6:
                raise CutsomException("No best Model found")
            logging.info("Best Model is founded")

            save_object(
                file_path=self.model_trainer_config.trainde_model_file_path,
                obj=best_model
            )
            predicted=best_model.predict(X_test)
            r2 = r2_score(y_test, predicted)
            return r2
        except Exception as e:
            raise CutsomException(e,sys)