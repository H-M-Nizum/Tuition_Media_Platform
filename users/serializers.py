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



class ApplicantRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']


    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']


        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Matched"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email ALready Exists."})

        account = User(username=username, email=email, first_name=first_name, last_name=last_name)
        # print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


# user password change serializer


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# update serializer
class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # def username(self):

    def update(self, instance):
        instance.username = self.validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        # instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        # instance.educational_qualification = validated_data.get('educational_qualification', instance.educational_qualification)
        instance.save()
        

        return instance