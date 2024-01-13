from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from . import models
from . import serializers

class ApplicationViewset(viewsets.ModelViewSet):
    queryset = models.ApplicationModel.objects.all()
    serializer_class = serializers.ApplicationSerializers

    # Custom query kortechi, particular applicant ar jonne, id ke dore
    def get_queryset(self):
        queryset = super().get_queryset()  ## applicant ke inherit korlam
        applicant_id = self.request.query_params.get('applicant_id')  ## applicant id ke niye aslam
        if applicant_id:  ## if applicant id exist kore
            queryset = queryset.filter(applicant_id=applicant_id) ## queryset ke overwrite korlam
        return queryset  # finally return queryset

   