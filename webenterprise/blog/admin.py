from django.contrib import admin
from .models import Category, Blog


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Publicar más columnas
    list_display = ('title','author','published')
    # Para ordenar por:
    ordering = ('published', 'author')
    # Buscador de entradas
    search_fields = ('title', 'content', 'author__username')
    # Navegación por fechas
    date_hierarchy = 'published'
    # Filtro
    list_filter = ('author__username',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)


