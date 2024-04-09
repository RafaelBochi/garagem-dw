from rest_framework.serializers import ModelSerializer

from app.models import Acessorio

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"