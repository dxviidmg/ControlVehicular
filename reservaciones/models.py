from django.db import models
from django.contrib.auth.models import User
from vehiculos.models import *
from django.utils import timezone

class Reservacion(models.Model):
	creacion = models.DateTimeField(default=timezone.now)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, null=True, blank=True)
	destino = models.TextField()
	asunto = models.TextField()
	salida = models.DateTimeField(default=timezone.now)
	llegada_aproximada = models.DateTimeField(default=timezone.now)
	llegada_real = models.DateTimeField(null=True, blank=True)

	class Meta:
		ordering = ('creacion',)

	def __str__(self):
		return '{} {}'.format(self.vehiculo, self.salida)

class Revision(models.Model):
	momento_choices = (
		('Llegada', 'Llegada'), 
		('Salida', 'Salida')
	)
	estado_choices = (
		('Excelente', 'Excelente'), 
		('Bueno', 'Bueno'),
		('Regular', 'Regular'), 
		('Malo', 'Malo'),
		('Pesimo', 'Pesimo'),				
	)	
	creacion = models.DateTimeField(default=timezone.now)
	reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE)
	momento = models.CharField(max_length=10, choices=momento_choices)
	kilometraje = models.IntegerField(null=True, blank=True)
	limpieza = models.CharField(max_length=10, choices=estado_choices)
	luces_bajas_delanteras = models.CharField(max_length=10, choices=estado_choices)
	aceite_motor = models.CharField(max_length=10, choices=estado_choices)
	liquido_frenos = models.CharField(max_length=10, choices=estado_choices)
	refrigerante = models.CharField(max_length=10, choices=estado_choices)
	indicador_cobustible = models.CharField(max_length=10, choices=estado_choices)
	indicador_temperatura = models.CharField(max_length=10, choices=estado_choices)
	indicador_aceite = models.CharField(max_length=10, choices=estado_choices)
	limpiaparabrisas = models.CharField(max_length=10, choices=estado_choices)
	gato_hidrauilico = models.CharField(max_length=10, choices=estado_choices)
	llave_birlos = models.CharField(max_length=10, choices=estado_choices)
	llanta_refraccion = models.CharField(max_length=10, choices=estado_choices)
	golpes_raspaduras = models.CharField(max_length=10, choices=estado_choices)
	presion_llantas = models.CharField(max_length=10, choices=estado_choices)
	bocina = models.CharField(max_length=10, choices=estado_choices)
	observaciones = models.TextField(null=True, blank=True)

	def __str__(self):
		return '{} {}'.format(self.reservacion, self.momento)	