from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from ...serializers.core.auth_serialize import UserSerializer
from ...services.core.http.response import new_response

User = get_user_model()


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"], url_path="register")
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                new_response(
                    mensaje="Usuario registrado exitosamente",
                    code="IN0002",
                    status=status.HTTP_201_CREATED,
                )
            )
        return Response(
            new_response(
                mensaje="Error en los datos enviados.",
                code="ER0001",
                status=status.HTTP_400_BAD_REQUEST,
                correcto=False,
                data=serializer.errors,
            )
        )

    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            print(user)
            return Response(
                new_response(
                    mensaje="Inicio de sesión exitoso.",
                    code="AU0002",
                    data={
                        "user": {
                            "id": user.id,
                            "email": user.email,
                            "username": user.username,
                            "email": user.email,
                        }
                    },
                    access_token=str(refresh.access_token),
                    token_type="bearer",
                    status=status.HTTP_200_OK,
                )
            )
        return Response(
            new_response(
                mensaje="Usuario o contraseña incorrectos.",
                code="AU0001",
                status=status.HTTP_401_UNAUTHORIZED,
                correcto=False,
            )
        )
