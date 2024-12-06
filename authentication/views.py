from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import UserRegisterSerializer

from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        # Создание нового пользователя
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Генерация JWT токенов для нового пользователя
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                "username": user.username,
                "access_token": access_token,
                "refresh_token": refresh_token
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
