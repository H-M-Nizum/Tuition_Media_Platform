from rest_framework import serializers
from . import models

# convert model object to JSON
class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUsModel
        fields = '__all__'