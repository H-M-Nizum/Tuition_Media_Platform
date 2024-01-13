from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from . import models
from . import serializers

class ContactUsViewset(viewsets.ModelViewSet):
    queryset = models.ContactUsModel.objects.all()
    serializer_class = serializers.ContactUsSerializers
