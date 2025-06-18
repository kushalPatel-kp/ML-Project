from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ModelPredictSerializer

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


class ModelPrediction(APIView):
    def post(self, request):
        serializer = ModelPredictSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            print(data['gender'])

            custom_data = CustomData(
                gender=data["gender"],
                race_ethnicity=data["race_ethnicity"],
                parental_level_of_education=data["parental_level_of_education"],
                lunch=data["lunch"],
                test_preparation_course=data["test_preparation_course"],
                reading_score=data["reading_score"],
                writing_score=data["writing_score"]
            )
            pred_df = custom_data.get_data_as_data_frame()
            print(pred_df)
            predict_pipeline = PredictPipeline()
            result = predict_pipeline.predict(pred_df)
            result_data={}
            result_data['result'] = result

            return Response(result_data, status=status.HTTP_200_OK)


