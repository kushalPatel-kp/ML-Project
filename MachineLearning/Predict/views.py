from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ModelPredictSerializer

# from pipeline.predict_pipeline import CustomData


class ModelPrediction(APIView):
    def post(self, request):
        serializer = ModelPredictSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            print(data['gender'])

            # custom_data = CustomData
            return Response(serializer.data, status=status.HTTP_200_OK)


