
from django.urls import path
from .views import celulares,Celular_Formulario,tablets,Tablet_Formulario,laptops,Laptop_Formulario, buscar,show_html

urlpatterns = [
    path('agregar_celular/', Celular_Formulario),
    path('agregar_tablet/', Tablet_Formulario),
    path('agregar_laptop/', Laptop_Formulario),
    path('celulares/', celulares),
    path('laptops/', laptops),
    path('tablets/', tablets),
    path('buscar/', buscar),
    path('show/', show_html),
]
