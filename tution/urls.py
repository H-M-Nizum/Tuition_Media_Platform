from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter() # amader router

router.register('class', views.TutionclassViewset) # router ar antena
router.register('list', views.TutionViewset) # router ar antena
router.register('review', views.ReviewViewset) # router ar antena

urlpatterns = [
    path('', include(router.urls)),
]
