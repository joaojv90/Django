from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.


def blog(request): # Esta solo es el nombre de la vista
    entry = Blog.objects.all()  # select
    return render(request, 'blog/blog.html', {'blog': entry}) # de nombre del diccionario va cualquiera y se pasa el dato de la variable donde se almacena todo

# Vista para ver las entradas por cada categoría
def category(request, categoryId):
    category = get_object_or_404(Category, id=categoryId) #para controlar y no dejar la información expuesta
    # cargar las entradas enlazadas a esa categoría
    #entry = Blog.objects.filter(categories=category)
    #return render(request, "blog/category.html", {'category': category, 'blog': entry})
    return render(request, "blog/category.html", {'category': category})
