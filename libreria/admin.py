from django.contrib import admin
from .models import NavItem, Autor, Categoria, Libro

# Register your models here.

admin.site.register(NavItem)
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Libro)

