from django.contrib import admin
from .models import *

class PerfilInline(admin.StackedInline):
	model = Perfil
	can_delete = False
	fk_name = 'user'

class LicenciaInline(admin.StackedInline):
	model = Licencia
	can_delete = False
	fk_name = 'user'

class UserAdmin(admin.ModelAdmin):
	inlines = [PerfilInline, LicenciaInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)