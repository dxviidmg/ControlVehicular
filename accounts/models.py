from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=15)	

	def __str__(self):
		return 'perfil de {}'.format(self.user)

class Licencia(models.Model):
	tipo_choices = (
		('A', 'A'),
		('B', 'B')
	)
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=1, default='A')
	sangre = models.CharField(max_length=10)
	restriccion = models.CharField(max_length=30)
	validez = models.DateField()
	titular_numero_emergencia = models.CharField(max_length=50)
	numero_emergencia = models.CharField(max_length=15)

	def __str__(self):
		return 'Licencia de {}'.format(self.user)

#Muestra nombre completo de la tabla Users	
def get_full_name(self):
	return '{} {} {}'.format(self.username, self.first_name, self.last_name)

User.add_to_class('__str__', get_full_name)	