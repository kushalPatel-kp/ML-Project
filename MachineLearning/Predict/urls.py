from django.urls import path
from Predict.views import ModelPrediction


urlpatterns = [
    path("check/", ModelPrediction.as_view(), name='check')
]
