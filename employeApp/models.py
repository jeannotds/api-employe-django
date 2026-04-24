from enum import unique
from django.db import models

class Departement(models.Model):
  nom_dept= models.CharField(max_length=100)
  data_embauche= models.DateTimeField(auto_now_add=True)

def __str__(self):
  return self.nom_dept

# Create your models here.
class  Employe(models.Model):
  nom= models.CharField(max_length=100)
  poste= models.CharField(max_length=100)
  salaire= models.DecimalField(max_digits=10, decimal_places=2)
  email= models.EmailField(unique=True)
  data_embauche= models.DateTimeField(auto_now_add=True)

  departement= models.ForeignKey(
    Departement,
    on_delete=models.CASCADE, #  Ça définit le comportement SI le département est supprimé
    related_name='employes',
    null=True, # autorise vide
    blank=True
  )

def __str__(self):
  return self.nom