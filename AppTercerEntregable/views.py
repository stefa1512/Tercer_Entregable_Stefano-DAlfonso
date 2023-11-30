from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "inicio.html")

def celulares(request):
    lista = Celular.objects.all()
    return render(request, "AppCoder/celulares.html",{"celular": lista})

def tablets(request):
    lista = Tablet.objects.all()
    return render(request, "AppCoder/tablets.html",{"tablet": lista})

def laptops(request):
    lista = Laptop.objects.all()
    return render(request, "AppCoder/laptops.html",{"laptop": lista})

def Celular_Formulario(request):
    if request.method == 'POST':
        prod_formulario = Celular_Formulario(request.POST)
        if prod_formulario.is_valid():
            data = prod_formulario.cleaned_data
            celular = Celular(marca= data['marca'], modelo= data['modelo'], almacenamiento= data['almacenamiento'])
            celular.save()
            return redirect ("AppCoder/show/")

        prod_formulario = Celular_Formulario()
        contexto = {
            "form": prod_formulario
        }
        return render(request, "AppCoder/celular_formulario.html", contexto)

def Tablet_Formulario(request):
    if request.method == 'POST':
        prod_formulario = Tablet_Formulario(request.POST)
        if prod_formulario.is_valid():
            data = prod_formulario.cleaned_data
            tablet = Celular(marca= data['marca'], modelo= data['modelo'], almacenamiento= data['almacenamiento'])
            tablet.save()
            return redirect ("AppCoder/show/")

        prod_formulario = Tablet_Formulario()
        contexto = {
            "form": prod_formulario
        }
        return render(request, "AppCoder/tablet_formulario.html", contexto)


def Laptop_Formulario(request):
    if request.method == 'POST':
        prod_formulario = Laptop_Formulario(request.POST)
        if prod_formulario.is_valid():
            data = prod_formulario.cleaned_data
            laptop = Celular(marca= data['marca'], modelo= data['modelo'], almacenamiento= data['almacenamiento'])
            laptop.save()
            return redirect ("AppCoder/show/")

        prod_formulario = Laptop_Formulario()
        contexto = {
            "form": prod_formulario
        }
        return render(request, "AppCoder/laptop_formulario.html", contexto)

def buscar(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        celulares = Celular.objects.filter(marca= marca)
        return render(request, "", {"celulares": celulares, "marca": marca})
    else:
        return HttpResponse("No se encuentra el equipo, ingrese un producto válido")

def show_html(request):
    contexto = {}
    return render(request,'base.html',contexto)
