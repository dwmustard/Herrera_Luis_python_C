from django import forms
from .models import Libros

class LibroForms (forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo','edicion','editorial','anio_de_publicacion','paginas']