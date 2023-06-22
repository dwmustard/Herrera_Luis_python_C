from django.db import models
from datetime import date

class Productos(models.Model):

    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"

    nombre = models.CharField("Nombre",max_length=300,default="")
    descripcion = models.CharField("Descripcion",max_length=300,default="")
    precio = models.DecimalField("Precio",max_digits=10,decimal_places=2,default=0)
    fecha_ingreso = models.DateField("Fecha de ingreso",auto_now_add=False,default=date.today)
    estatus = models.CharField("Estatus",max_length=300,default="")
    
    def _str_(self):
        return self.nombre