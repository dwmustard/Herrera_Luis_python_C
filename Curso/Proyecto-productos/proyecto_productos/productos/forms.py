from django import forms
from .models import Productos

class ProductosForms (forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre','descripcion','precio','fecha_ingreso','estatus']
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')
        precio = cleaned_data.get('precio')
        fecha_ingreso = cleaned_data.get('fecha_ingreso')
        estatus = cleaned_data.get('estatus')
        
        if not nombre or not descripcion or not precio or not fecha_ingreso or not estatus:
            raise forms.ValidationError('Todos los campos deben llenarse')
        
        return cleaned_data