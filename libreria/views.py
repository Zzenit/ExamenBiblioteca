from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    navbar = Navbar.objects.all()
    context = {'navbar':navbar}
    return render(request, 'libreria/index.html', context)

def libros(request):
    navbar = Navbar.objects.all()
    libros = Libros.objects.all()
    context = {'navbar':navbar, 'libros': libros}
    return render(request, 'libreria/libros.html', context)

def autores(request):
    navbar = Navbar.objects.all()
    autores = Autores.objects.all()
    context = {'navbar':navbar, 'autores': autores}
    return render(request, 'libreria/autores.html', context)

def categorias(request):
    navbar = Navbar.objects.all()
    categorias = Categorias.objects.all()
    context = {'navbar':navbar, 'categorias': categorias}
    return render(request, 'libreria/categorias.html', context)