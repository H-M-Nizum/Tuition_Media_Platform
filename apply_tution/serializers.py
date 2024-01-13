from rest_framework import serializers
from . import models

# convert model object to JSON
class ApplicationSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.ApplicationModel
        fields = '__all__'