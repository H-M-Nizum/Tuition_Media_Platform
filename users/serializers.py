from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

# convert model object to JSON
class ApplicantSerializers(serializers.ModelSerializer):
    # OneToOne, ManyToMany, Forigenkey relational model ar id ar poriborte name show korar jonne use kora hoy.
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.ApplicantModel
        fields = '__all__'


