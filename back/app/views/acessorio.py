from rest_framework.viewsets import ModelViewSet

from app.models import Acessorio
from app.serializers import AcessorioSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer