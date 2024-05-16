from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Persona)
admin.site.register(models.Provedor)
admin.site.register(models.Posicion)
admin.site.register(models.Producto)
admin.site.register(models.Trabajador)
