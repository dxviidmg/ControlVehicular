from django.shortcuts import render
from django.views.generic import View
from .models import *
from reservaciones.models import *
from django.db.models import Q
from django.utils import timezone
now = timezone.now()

class VehiculosListView(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = 'vehiculos/vehiculos_list.html'
		vehiculos = Vehiculo.objects.all()

		vehiculos_list = []

		for vehiculo in vehiculos:
			reservaciones = Reservacion.objects.filter(vehiculo=vehiculo, salida__lte=now)
			reservaciones = reservaciones.filter(Q(llegada_aproximada__gte=now) | Q(llegada_real__isnull=True))

			print("test de carro", vehiculo)
			if reservaciones:
#				print(vehiculo, "ocupado")			
				for reservacion in reservaciones:
					revisiones = Revision.objects.filter(reservacion=reservacion)
					
				if len(revisiones) == 0:
#					print(vehiculo, reservacion, "Apartado")
					vehiculos_list.append({'vehiculo': vehiculo, 'ubicacion': 'Palma Gorda', 'status': 'Apartado', 'user': reservacion.user})
				if len(revisiones) == 1:
#					print(vehiculo, reservacion, "Ocupado")
					vehiculos_list.append({'vehiculo': vehiculo, 'ubicacion': reservacion.destino, 'status': 'Ocupado', 'user': reservacion.user})
			else:
#				print(vehiculo, 'libre')
				vehiculos_list.append({'vehiculo': vehiculo, 'ubicacion': 'Palma Gorda', 'status': 'Disponible'})
#			if len(reservaciones) != 0:
#				reservaciones2 = reservaciones.objects()
		print("lista de dict")
		print(vehiculos_list)
#		ListOfChannelsByCategory = []

#		for category in categories:
#			ListOfChannelsByCategory.append({'category': category.name, 'channels': Channel.objects.filter(category=category, link_status="Functional")})

		context = {
#			'ListOfChannelsByCategory': ListOfChannelsByCategory,
			'vehiculos_list': vehiculos_list
		}
		return render(request, template_name, context)