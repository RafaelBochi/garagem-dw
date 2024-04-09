from rest_framework.viewsets import ModelViewSet

from app.models import Cor
from app.serializers import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer