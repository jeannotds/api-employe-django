from django.urls import path

from .import views

urlpatterns = [
      path('employes/', views.employe_list)
  ]