from rest_framework import serializers


class ModelPredictSerializer(serializers.Serializer):
    gender = serializers.CharField()
    race_ethnicity = serializers.CharField()
    parental_level_of_education = serializers.CharField()
    lunch = serializers.CharField()
    test_preparation_course = serializers.CharField()
    reading_score = serializers.IntegerField()
    writing_score = serializers.IntegerField()
    