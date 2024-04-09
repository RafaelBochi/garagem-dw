from rest_framework.viewsets import ModelViewSet

from app.models import Categoria
from app.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer