from django.db import models

# Create your models here.
class Navbar(models.Model):
    id_nav = models.AutoField(db_column="idNav", primary_key=True)
    nom_nav = models.CharField(max_length=20, blank=False, null=False)
    url_nav = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
	    return str(self.nom_nav)

class Autores(models.Model):
    id_autor = models.AutoField(db_column="idAutor",primary_key=True)
    nom_autor = models.CharField(max_length=50, blank=False, null=False)
    nacionalidad_autor = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return str(self.nom_autor)

class Categorias(models.Model):
    id_categoria = models.AutoField(db_column="idCategoria", primary_key=True)
    nom_categoria = models.CharField(max_length=50, blank=False, null=False)
    desc_categoria = models.TextField(max_length=500, blank=False, null=False)
    def __str__(self):
        return str(self.nom_categoria)

class Libros(models.Model):
    id_libro = models.AutoField(db_column="idLibro", primary_key=True)
    titulo_libro = models.CharField(max_length=50, blank=False, null=False)
    anio_publicacion = models.CharField(max_length=5, blank=False, null=False)
    desc_libro = models.TextField(max_length=500, blank=False, null=False)
    def __str__(self):
        return str(self.titulo_libro)