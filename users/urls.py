from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter() # amader router

router.register('list', views.ApplicantViewset) # router ar antena

urlpatterns = [
    path('', include(router.urls)),  
    path('register/', views.ApplicantRegisterViewsset.as_view(), name='register'), 
    path('login/', views.UserLoginApiview.as_view(), name='login'),
    path('adminlogin/', views.AdminLoginApiview.as_view(), name='adminlogin'),
    path('adminlogout/', views.AdminLogoutAPIView.as_view(), name='adminlogout'),
    path('update/', views.UpdateUser.as_view(), name='update'),
    path('pass_change/', views.ChangePasswordView.as_view(), name='pass_change'),
    path('active/<uid64>/<token>/', views.activate, name='activate')
]
