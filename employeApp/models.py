from enum import unique
from django.db import models

# Create your models here.
class  Employe(models.Model):
  nom= models.CharField(max_length=100)
  poste= models.CharField(max_length=100)
  salaire= models.DecimalField(max_digits=10, decimal_places=2)
  email= models.EmailField(unique=True)
  data_embauche= models.DateTimeField(auto_now_add=True)

def __str__(self):
  return self.nom