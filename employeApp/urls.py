from django.urls import path

from .import views

urlpatterns = [
      path('employes/', views.employe_list),
      path('employes/post', views.create_employe),
      path('employes/<int:id>/update', views.update_employe),
      path('employes/<int:id>/delete', views.delete_employe)
  ]