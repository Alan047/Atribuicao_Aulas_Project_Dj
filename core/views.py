from django.shortcuts import render
from .models import Semestre, Professor, Curso

def home(request):
    return render(request, 'home.html')

def semestre(request):
    semestre = Semestre.objects.all().order_by('-id')
    context = {
        'semestre':semestre
    }
    return render(request, 'semestre.html', context)

def professores(request):
    professor = Professor.objects.all()
    context = {
        'professor':professor
    }
    return render(request, 'professores.html', context)

def select_semestre(request, id):
    semestre = Semestre.objects.get(pk=id)
    curso = Curso.objects.all()
    context = {
        'semestre' : semestre,
        'curso': curso
    }
    return render(request, 'select_semestre.html', context)

def cursos_list_page(request):
    curso = Curso.objects.all()
    context = {
        'curso': curso
    }
    return render(request, 'curso_list_page.html', context)

