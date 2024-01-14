from django.shortcuts import render, redirect
from .models import Semestre, Professor, Curso, Disciplina
from .forms import SemestreForm

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

def disciplinas_list(request):
    disciplinas = Disciplina.objects.filter(periodo__isnull=False).extra(where=['"core_disciplina"."periodo" % 2 = 0'])
    print(disciplinas)
    context = {
        'disciplinas': disciplinas
    }
    return render(request, 'disciplinas.html', context)

def adicionar_semestre(request):
    form = SemestreForm()
    disciplinas = Disciplina.objects.filter(periodo__isnull=False).extra(where=['"core_disciplina"."periodo" % 2 = 0'])
    print(disciplinas)
    if request.method == 'POST':
        form = SemestreForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.disciplinas = disciplinas[0]
            form.save()
        return redirect('/adicionar_semestre')
    context = {
        'form':form
    }
    return render(request, 'adicionar_semestre.html', context)

