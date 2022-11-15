from django.shortcuts import render
from .models import Blog

# Create your views here.


def blog(request): # Esta solo es el nombre de la vista
    entry = Blog.objects.all()  # select
    return render(request, 'blog/blog.html', {'blog': entry}) # de nombre del diccionario va cualquiera y se pasa el dato de la variable donde se almacena todo
