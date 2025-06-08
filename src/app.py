from flask import Flask, request, render_template, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app=application

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/prediction", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = request.get_json()
        custom_data = CustomData(
            gender=data['gender'],
            race_ethnicity=data['race_ethnicity'],
            parental_level_of_education=data['parental_level_of_education'],
            lunch=data['lunch'],
            test_preparation_course=data['test_preparation_course'],
            reading_score=data['reading_score'],
            writing_score=data['writing_score']
        )

        pred_df = custom_data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)
        return jsonify({
            "math_score_prediction": result[0]
        })
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)