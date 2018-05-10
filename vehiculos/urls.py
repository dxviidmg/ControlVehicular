from .views import *
from django.urls import path

app_name = 'vehiculos'
urlpatterns = [
	path('vehiculos/', VehiculosListView.as_view(), name='vehiculos-list'),
]