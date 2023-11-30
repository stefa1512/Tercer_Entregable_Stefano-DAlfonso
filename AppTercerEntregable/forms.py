from django import forms

class Celular_Formulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    almacenamiento = forms.IntegerField()


class Tablet_Formulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    almacenamiento = forms.IntegerField()


class Laptop_Formulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    almacenamiento = forms.IntegerField()
