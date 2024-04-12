from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .models import Usuario
from .serializers import UsuarioSerializer
from .functions import LoginFunction, RegisterFunction

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def login(request):
    username_or_email = request.data.get("username_or_email")
    password = request.data.get("password")

    response = LoginFunction(username_or_email, password)

    if response["code"] == 200:
        return Response(response, status=status.HTTP_200_OK)
    elif response["code"] == 400:
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def register(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    response = RegisterFunction(username, email, password)

    if response["code"] == 201:
        return Response(response, status=status.HTTP_201_CREATED)
    elif response["code"] == 400:
        return Response(response, status=status.HTTP_400_BAD_REQUEST)