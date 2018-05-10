from django.contrib import admin
from .models import *

#admin.site.register(Reservacion)
#admin.site.register(Revision)

class RevisionInline(admin.StackedInline):
	model = Revision
	can_delete = False
	fk_name = 'reservacion'

class ReservacionAdmin(admin.ModelAdmin):
	inlines = [RevisionInline]

admin.site.register(Reservacion, ReservacionAdmin)