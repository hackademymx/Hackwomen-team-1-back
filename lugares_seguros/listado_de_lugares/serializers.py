from rest_framework import serializers
from.models import listado_de_lugares

class listado_de_lugaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = listado_de_lugares
        fields = '_all_'
