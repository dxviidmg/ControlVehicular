from django.db import models
from datetime import datetime

now = datetime.now()

class Vehiculo(models.Model):
	status_choices = (
		('Disponible', 'Disponible'), 
		('Ocupado', 'Ocupado'),
		('En taller', 'En taller'),		
	)
	
	marca = models.CharField(max_length=30)
	submarca = models.CharField(max_length=30)
	clase = models.CharField(max_length=30)
	tipo = models.CharField(max_length=30)
	modelo = models.IntegerField()
	numero = models.IntegerField(null=True, blank=True, unique=True)
	numero_serie = models.CharField(max_length=30, unique=True)
	placa = models.CharField(max_length=10, unique=True)
	color = models.CharField(max_length=10)
	nombre = models.CharField(max_length=10)
	kilometraje = models.IntegerField()
	status = models.CharField(max_length=10, default="Disponible", choices=status_choices)

	class Meta:
		ordering = ('nombre',)

	def __str__(self):
		return '{} {}'.format(self.nombre, self.placa)

class Documentacion(models.Model):
#	now = datetime.now()
	año = int(now.year)

	meses_choices = (
		('Enero y febrero', 'Enero y febrero'), 
		('Febrero y marzo', 'Febrero y marzo'),
		('Marzo y abril', 'Marzo y abril'),
		('Abril y mayo', 'Abril y mayo'), 
		('Mayo y junio', 'Mayo y junio'),
		('Junio y julio', 'Junio y julio'),
		('Julio y agosto', 'Julio y agosto'), 
		('Agosto y septiembre', 'Agosto y septiembre'),
		('Septiembre y octubre', 'Septiembre y octubre'),
		('Octubre y noviembre', 'Octubre y noviembre'), 
		('Noviembre y diciembre', 'Noviembre y diciembre'),
		('Diciembre y enero', 'Diciembre y enero'),						
	)

	año_choices = [(i,str(i)) for i in range((año-1),(año+2))]

	vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
	meses_proxima_verificacion = models.CharField(max_length=25, choices=meses_choices)
	año_proxima_verificacion = models.IntegerField(choices=año_choices)
	verificacion = models.FileField(upload_to='verificacion/%Y/%m/%d/')
	tarjeta_circulacion = models.FileField(upload_to='circulacion/%Y/%m/%d/')

	def __str__(self):
		return '{}'.format(self.vehiculo)

class Aseguradora(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return '{}'.format(self.nombre)

class Seguro(models.Model):
	vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
	aseguradora = models.ForeignKey(Aseguradora, on_delete=models.CASCADE)
	validez = models.DateField()
	numero_poliza = models.CharField(max_length=15)
	inciso = models.CharField(max_length=15)
	poliza = models.FileField(upload_to='polizas/%Y/%m/%d/')

	def __str__(self):
		return '{}'.format(self.vehiculo)