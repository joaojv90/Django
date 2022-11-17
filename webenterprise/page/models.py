from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='Titulo',max_length=200)
    content = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['title']

    def __str__(self):
        return self.title
