from django.db import models

# Create your models here.
class NavItem(models.Model):
    titulo = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
	    return str(self.titulo)


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
	    return str(self.nombre)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
	    return str(self.nombre)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    año_publicacion = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
	    return str(self.titulo)