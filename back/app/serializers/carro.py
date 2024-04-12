from rest_framework.serializers import ModelSerializer

from app.models import Carro

class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"

class CarroDetailSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"
        depth = 1