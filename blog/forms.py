from django import forms
from .models import Entrada,Categoria

class FormularioEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('categoria','titulo','contenido','imagen')

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)