from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter() # amader router

router.register('list', views.ApplicantViewset) # router ar antena

urlpatterns = [
    path('', include(router.urls)),  
    path('register/', views.ApplicantRegisterViewsset.as_view(), name='register'), 
    path('login/', views.UserLoginApiview.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name='activate')
]
