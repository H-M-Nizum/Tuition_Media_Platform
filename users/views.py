from django.shortcuts import render, redirect
from rest_framework import viewsets
# Create your views here.

from . import models
from . import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  




class ApplicantViewset(viewsets.ModelViewSet):
    queryset = models.ApplicantModel.objects.all()
    serializer_class = serializers.ApplicantSerializers

class ApplicantRegisterViewsset(APIView):
    serializer_class = serializers.ApplicantRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            print(user)
            print(user.email)

            token = default_token_generator.make_token(user)
            print('token', token)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(uid)

            confirm_link = f"http://127.0.0.1:8000/user/active/{uid}/{token}"

            email_subject = 'Çonfirm your email'
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response(" Check Your mail for confirmation")
        return Response(serializer.errors)



def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except (user.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("login")
    else:
        return redirect("register")




class UserLoginApiview(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'úser_id': user.id})
            else:
                return Response({'error' : 'Invalid User'})

        return Response(serializer.errors)


class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect("login")




class AdminLoginApiview(APIView):
    def post(self, request):
        serializer = serializers.AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user and user.is_superuser:
                login(request, user)
                return Response('successful')
            else:
                return Response({'error': 'Invalid User'})

        return Response(serializer.errors)



class AdminLogoutAPIView(APIView):
    def get(self, request):
        logout(request)
        return redirect("adminlogin")


# user password change views

class ChangePasswordView(generics.UpdateAPIView):
        serializer_class = serializers.ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()

                return redirect("login")

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# update profile
class UpdateUser(generics.UpdateAPIView):
    serializer_class = serializers.UpdateUserSerializer
    queryset = User.objects.all()