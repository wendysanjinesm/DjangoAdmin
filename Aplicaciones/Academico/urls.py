from . import views
from django.urls import path

urlpatterns = [ 
    path('home', views.home),
    path('gestionCurso', views.gestionCurso),
    path('nuevoCurso/',views.nuevoCurso),
    path('registrarCurso/',views.registrarCurso),
    path('edicionCurso/<codigo>',views.edicionCurso),
    path('editarCurso/<codigo>',views.editarCurso),
    path('eliminarCurso/<codigo>',views.eliminarCurso)
]