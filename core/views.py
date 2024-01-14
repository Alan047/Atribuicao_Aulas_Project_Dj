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

def disciplinas_list(request, id, id2):
    semestre = Semestre.objects.get(pk=id2)
    curso = Curso.objects.get(pk=id)
    disciplinas = curso.disciplina_set.all().filter(semestre=semestre)

    print(semestre)
    print(disciplinas.filter(semestre=semestre))
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
            semestre = form.save(commit=False)
            semestre.save()
            semestre.disciplinas.set(disciplinas)
            cursos = form.cleaned_data['cursos']
            semestre.cursos.set(cursos)
        return redirect('/adicionar_semestre')
    context = {
        'form':form
    }
    return render(request, 'adicionar_semestre.html', context)

