from django.shortcuts import render,redirect
from .models import Curso
from django.contrib import messages

# Create your views here.
def gestionCurso(request):
    cursos=Curso.objects.all()    
    return render(request,"gestionCursos.html",{ "cursos": cursos })

def home(request):
    return render(request,'index.html')

def nuevoCurso(request):
    return render(request,'nuevoCurso.html')

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['txtCreditos']
    curso=Curso.objects.create( codigo=codigo, nombre=nombre , creditos=creditos )
    messages.success(request,'!Curso Registrado!')
    return redirect('/gestionCurso')

def eliminarCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    messages.success(request,'!Curso Eliminado!')
    curso.delete()
    return redirect('/gestionCurso')

def editarCurso(request,codigo):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['txtCreditos']    
    curso= Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    messages.success(request,'!Curso Editado!')
    return redirect('/gestionCurso')

def edicionCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request,'edicionCurso.html', { "curso": curso })