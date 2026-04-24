from rest_framework import serializers
from .models import Departement, Employe


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'


class EmployeSerializer(serializers.ModelSerializer):
    departement = DepartementSerializer(read_only=True)

    departement_id = serializers.PrimaryKeyRelatedField(
        queryset=Departement.objects.all(),
        source='departement',
        write_only=True
    )

    class Meta:
        model = Employe
        fields = '__all__'