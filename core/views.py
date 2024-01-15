from django.shortcuts import render, redirect
from .models import Semestre, Professor, Curso, Disciplina
from .forms import SemestreForm
from django.contrib.auth.forms import AuthenticationForm

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
    if request.method == 'POST':
        disciplinas_pares = Disciplina.objects.filter(periodo__isnull=False).extra(where=['"core_disciplina"."periodo" % 2 = 0'])
        disciplinas_impares = Disciplina.objects.filter(periodo__isnull=False).extra(where=[' "core_disciplina"."periodo" % 2 > 0'])
        form = SemestreForm(request.POST)
        print(request.POST['periodos'])
        if form.is_valid():
            semestre = form.save(commit=False)
            semestre.save()
            if request.POST['periodos'] == 'impar':
                semestre.disciplinas.set(disciplinas_impares)
                print('entrou no impar')
            if request.POST['periodos'] == 'par':
                semestre.disciplinas.set(disciplinas_pares)
                print('entrou no par')
            semestre.cursos.set(form.cleaned_data['cursos'])
            semestre.disciplinas.set(form.cleaned_data['disciplinas'])
        return redirect('/adicionar_semestre')
    context = {
        'form':form
    }
    return render(request, 'adicionar_semestre.html', context)

def login_view(request):
    form = AuthenticationForm(request)
    context = {
        'form ' : form,
    }

    print(form)

    return render(request, 'login.html', {
        'form':form
    })

