from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.http import Http404
from django.utils.crypto import get_random_string
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from news import settings
from users.models import User
from users.models import VerificationCode
from users.serializer import UserSerializer, RegisterSerializer, LoginSerializer, CustomTokenObtainSerializer, \
    UserDetailSerializer, SendEmailVerificationCodeSerializer


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reuqest, *args, **kwargs):
        serializer = UserSerializer(reuqest.user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = UserSerializer(instance=request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = User.objects.filter(email=email).first()
        if user:
            authenticate(request, password=password, email=email)
            return Response(serializer.data)
        else:
            raise Http404


class SendEmailVerificationCode(APIView):
    @swagger_auto_schema(request_body=SendEmailVerificationCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = SendEmailVerificationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        code = get_random_string(allowed_chars='123456789', length=6)
        VerificationCode.objects.create(email=email, code=code)
        subject = 'Verification'
        messages = f'Hi {email},Your verification code is  {code} for ERKINOV 🎱 website. Don''t give anyone'
        send_mail(subject, messages, from_email=settings.EMAIL_HOST_USER, recipient_list=[email])
        return Response({"detail": 'Sent successfully '})
