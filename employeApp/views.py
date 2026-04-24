from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employeApp.serializers import EmployeSerializer
from .models import Employe

# Create your views here.

@api_view(['GET', 'POST'])
def employe_list(request):
  if request.method == 'GET':
    employes = Employe.objects.all();
    serializer = EmployeSerializer(employes, many=True)
    return Response(serializer.data);

  if request.method == 'POST':
    serializer = EmployeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)