from django.db import models

# Create your models here.
class Project(models.Model):
    #atributos
    title = models.CharField(max_length=200, verbose_name='Titulo') #tipo de dato para cadena de caracteres
    # permite utilizar varios párrafos
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen',upload_to='projects')
    # Es recomendable crear fechas de creación y de modificación
    # permite tomar la fecha al crear un proyecto
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    # captura la fecha cuando se ejecuta algún cambio
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    link = models.URLField(verbose_name='Enlace de proyecto',null=True, blank=True)

# Subclase
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        #ordenar la lista de objetos
        ordering = ['-created'] #Si se coloca el - antes de la palabra ordena del más actual al más antiguo

    def __str__(self):
        return self.title #de esta manera muestra el nombre del proyecto