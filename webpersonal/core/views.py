from django.shortcuts import render, HttpResponse

# Create your views here.

# Vista home
def home(request):
    return render(request, "core/home.html")

# About-me
def about(request):
    return render(request, "core/about.html")

# Contact
def contact(request):
    return render(request, "core/contact.html")
