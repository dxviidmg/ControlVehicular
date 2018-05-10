from django.contrib import admin
from .models import *

#admin.site.register(Vehiculo)
#admin.site.register(Documentacion)
admin.site.register(Aseguradora)
#admin.site.register(Seguro)

class DocumentacionInline(admin.StackedInline):
    model = Documentacion
    can_delete = False
    fk_name = 'vehiculo'

class SeguroInline(admin.StackedInline):
    model = Seguro
    can_delete = False
    fk_name = 'vehiculo'    

class VehiculoAdmin(admin.ModelAdmin):
    inlines = [DocumentacionInline, SeguroInline]

admin.site.register(Vehiculo, VehiculoAdmin)