from django.urls import path
from matecoder.views import inicio, cursos,  estudiantes, profesores, entregables
urlpatterns = [
    path('cursos/', cursos, name='cursos'),
    path('', inicio, name='inicio'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('profesores/', profesores, name='profesores'),
    path('entregables/', entregables, name='entregables'),
]
