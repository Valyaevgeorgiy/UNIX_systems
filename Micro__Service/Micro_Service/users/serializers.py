from rest_framework import serializers
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["id", "username", "password"]


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255)


class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return validated_data