from rest_framework.viewsets import ModelViewSet

from app.models import Carro
from app.serializers import CarroSerializer, CarroDetailSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CarroDetailSerializer
        return CarroSerializer