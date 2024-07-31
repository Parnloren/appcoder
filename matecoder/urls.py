from django.urls import path
from matecoder.views import inicio, cursos,  estudiantes, profesores, entregables
urlpatterns = [
    path('curso/', cursos),
    path('', inicio),
    path('estudiante/', estudiantes),
    path('profesor/', profesores),
    path('entregable/', entregables),
]
