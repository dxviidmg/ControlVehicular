from django.urls import path
from .views import *

app_name = 'vehiculos'

urlpatterns = [
	path('vehiculo/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo-detail'),
	path('vehiculos/', VehiculosListView.as_view(), name='vehiculos-list'),
]