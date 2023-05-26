from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.http import Http404
from django.utils.crypto import get_random_string
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from news import settings
from users.models import User
from users.models import VerificationCode
from users.serializer import UserSerializer, RegisterSerializer, LoginSerializer, CustomTokenObtainSerializer, \
    SendEmailVerificationCodeSerializer, CheckEmailVerificationCodeSerializer


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

    def get(self, reqest, *args, **kwargs):
        serializer = UserSerializer(reqest.user)
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


class CHeckEmailVerificationCodes(CreateAPIView):
    queryset = VerificationCode.objects.all()
    serializer_class = CheckEmailVerificationCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        code = serializer.validated_data.get('code')
        verification_code = self.get_queryset().filter(email=email, is_verified=False).order_by(
            "-last_sent_time").first()
        if verification_code and verification_code.code != code and verification_code.is_expire:
            raise ValidationError("Verification code invalid.")
        verification_code.is_verified = True
        verification_code.save(update_fields=["is_verified"])
        return Response({"detail": "Verification code is verified"})


class CheckEmailVerificationCodeWithParams(APIView):
    def get(self, request, *args, **kwargs):
        email = request.query_params.get("email")
        code = request.query_params.get("code")
        verification_code = (
            VerificationCode.objects.filter(email=email, is_verified=False)

        )
        if verification_code and verification_code.code != code:
            raise ValidationError("Verification code verified.")
        verification_code.is_verified = True
        verification_code.save(update_fields=["is_verified"])
        return Response({"detail": "Verification code is verified."})


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
