from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample, name='sample'),
    path('<int:pageId>', views.sample, name='sample')
]
