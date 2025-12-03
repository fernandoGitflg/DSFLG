from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                 
    path('mi_primera_vista/', views.mi_primera_vista, name='mi_primera_vista'),
    path('listar_personas/', views.listar_personas, name='listar_personas')
]