from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .serializers import CreateUserSerializer, PasswordSerializer, UserTokenSerializer, UserInfoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    @action(url_path='info', methods=['GET'], detail=False,
            permission_classes=[permissions.IsAuthenticated])
    def user_info(self, request):
        user = request.user
        return Response({'info': UserInfoSerializer(user).data})

    @action(url_path='create', methods=['POST'], detail=False,
            permission_classes=[permissions.AllowAny])
    def create_user(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            try:
                validate_password(password)
                user = User.objects.create_user(
                    username=serializer.validated_data['username'],
                    password=serializer.validated_data['password'],
                    email=serializer.validated_data.get('email'))
                return Response({'Created successfully!': user.username})
            except ValidationError as e:
                return Response(str(e), status.HTTP_404_NOT_FOUND)
        return Response({'errors': serializer.errors}, status.HTTP_404_NOT_FOUND)

    @action(url_path='password', methods=['POST'], detail=False,
            permission_classes=[permissions.IsAuthenticated])
    def set_password(self, request):
        user = request.user
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            try:
                validate_password(password)
                user.set_password(serializer.validated_data['password'])
                user.save()
                return Response({'status': 'password set'})
            except ValidationError as e:
                return Response(str(e), status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @action(url_path='token', methods=['POST'], detail=False,
            permission_classes=[permissions.AllowAny])
    def get_token(self, request):
        serializer = UserTokenSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username, password)
            user = get_object_or_404(User, username=username)
            if check_password(password, user.password):
                print('correct pass')
                token = AccessToken.for_user(user)
                return Response({'token': str(token)},
                                status=status.HTTP_200_OK)
            return Response({'error': 'Wrong password'})
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)