from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'matecoder/inicio.html')
def cursos(request):
    return render(request, 'matecoder/cursos.html')

def estudiantes(request):
    return render(request, 'matecoder/estudiantes.html')

def profesores(request):
    return render(request, 'matecoder/profesores.html')

def entregables(request):
    return render(request, 'matecoder/entregables.html')
