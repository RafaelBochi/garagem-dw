from rest_framework.viewsets import ModelViewSet

from app.models import Marca
from app.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer