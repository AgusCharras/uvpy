from django.shortcuts import render
from .models import Carrera

def home(request):
    return render(request, 'home.html')

def ver_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, "carreras.html", {'carreras': carreras})