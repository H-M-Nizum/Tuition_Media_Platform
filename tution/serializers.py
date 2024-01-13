from rest_framework import serializers
from . import models

# convert model object to JSON
class TutionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.TutionModel
        fields = '__all__'

class TutionClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.TutionClassModel
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ReviewModel
        fields = '__all__'