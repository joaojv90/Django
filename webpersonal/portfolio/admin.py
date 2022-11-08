from django.contrib import admin
from .models import Project #al colocar el . antes de la clase es porque está dentro de la misma carpeta

# Crear una clase para configuraciones extendidas (adicionales)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

# Register your models here.
admin.site.register(Project, ProjectAdmin)
