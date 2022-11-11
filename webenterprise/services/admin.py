from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #De esta manera se muestran los campos ocultos

admin.site.register(Service, ServiceAdmin) # Aumentar aquí toda configuración extendida
