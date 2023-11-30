
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('agregar_celular/', Celular_Formulario),
    path('agregar_tablet/', Tablet_Formulario),
    path('agregar_laptop/', Laptop_Formulario),
    path('celulares', celulares),
    path('laptops', laptops),
    path('tablets', tablets),
    path('inicio', inicio),
    path('buscar', buscar),

]
