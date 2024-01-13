from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework import filters, pagination
from . import models
from . import serializers


class TutionclassViewset(viewsets.ModelViewSet):
    queryset = models.TutionClassModel.objects.all()
    serializer_class = serializers.TutionClassSerializers



class TutionPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100



class TutionViewset(viewsets.ModelViewSet):
    queryset = models.TutionModel.objects.all()
    serializer_class = serializers.TutionSerializers
    filter_backends = [filters.SearchFilter]

    pagination_class = TutionPagination
    search_fields = ['subject', 'tutionclass__name']




class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.ReviewModel.objects.all()
    serializer_class = serializers.ReviewSerializers

