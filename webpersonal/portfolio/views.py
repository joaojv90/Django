from django.shortcuts import render
from .models import Project

# Create your views here.
# Portfolio
def portfolio(request):
    # en esta variabele se guardarían los proyectos creados desde el admin
    projects = Project.objects.all() # De esta manera se realizaría el select de la información de la tabla project
    return render(request, "portfolio/portfolio.html",{'projects' : projects}) # así se pasa la información al template
