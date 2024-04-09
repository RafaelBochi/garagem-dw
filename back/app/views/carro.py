from rest_framework.viewsets import ModelViewSet

from app.models import Carro
from app.serializers import CarroSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer