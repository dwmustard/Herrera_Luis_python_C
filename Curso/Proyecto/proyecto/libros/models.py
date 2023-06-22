from django.db import models

# Create your models here.
class Libros(models.Model):

    class Meta:
        verbose_name = "Libros"
        verbose_name_plural = "Libros"

    titulo = models.CharField("Titulo",max_length=300,default="")
    edicion = models.CharField("Edicion",max_length=300,default="")
    editorial = models.CharField("Editorial",max_length=300,default="")
    anio_de_publicacion = models.IntegerField("Año de publicacion",default=0)
    paginas = models.IntegerField("No. de Paginas",default=0)
    
    def _str_(self):
        return self.titulo