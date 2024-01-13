from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter() # amader router

router.register('list', views.ApplicationViewset) # router ar antena

urlpatterns = [
    path('', include(router.urls)),
]
