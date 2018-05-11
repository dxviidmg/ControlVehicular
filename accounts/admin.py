from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class PerfilInline(admin.StackedInline):
	model = Perfil
	can_delete = False
	fk_name = 'user'

class LicenciaInline(admin.StackedInline):
	model = Licencia
	can_delete = False
	fk_name = 'user'

#class UserAdmin(admin.ModelAdmin):
#	inlines = [PerfilInline, LicenciaInline]

#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)

class CustomUserAdmin(UserAdmin):
	inlines = [PerfilInline, LicenciaInline]    
#inlines = (PerfilInline, SistemaBebederosInline)

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)	    