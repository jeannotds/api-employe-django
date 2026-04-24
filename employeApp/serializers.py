from rest_framework import serializers
# from employeApp.models import Employe
from .models import Departement, Employe


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model= Departement
        fiels = '__all__'