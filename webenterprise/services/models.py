from django.db import models

# Create your models here.
#El modelo es importante trabajarlos en singular

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    image = models.ImageField(verbose_name='Image', upload_to='services')
    # upload_to -> crea una carpeta dentro de la ruta donde se va a guardar la imagen
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    # auto_now_add captura automáticamente la fecha del sistema una sola vez cuando se crea
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    # auto_now captura automáticamente la fecha del sistema cada que se realiza un cambio

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title
