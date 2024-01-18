from django.shortcuts import render, redirect
from .models import Semestre, Professor, Curso, Disciplina
from .forms import SemestreForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def home(request):
    return render(request, 'home.html')
@login_required(login_url="/login")
def semestre(request):
    semestre = Semestre.objects.all().order_by('-id')
    context = {
        'semestre':semestre
    }
    print(dir(request))
    print(request.path_info)
    return render(request, 'semestre.html', context)

@login_required(login_url="/login")
def professores(request):
    professor = Professor.objects.all()
    context = {
        'professor':professor
    }
    return render(request, 'professores.html', context)

@login_required(login_url="/login")
def select_semestre(request, id):
    semestre = Semestre.objects.get(pk=id)
    curso = Curso.objects.all()
    context = {
        'semestre' : semestre,
        'curso': curso
    }
    return render(request, 'select_semestre.html', context)

@login_required(login_url="/login")
def cursos_list_page(request):
    curso = Curso.objects.all()
    context = {
        'curso': curso
    }
    return render(request, 'curso_list_page.html', context)

@login_required(login_url="/login")
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

@login_required(login_url="/login")
def adicionar_semestre(request):
    form = SemestreForm()
    if request.method == 'POST':
        disciplinas_pares = Disciplina.objects.filter(periodo__isnull=False, impar_par='par')
        disciplinas_impares = Disciplina.objects.filter(periodo__isnull=False, impar_par='impar')
        print(request.POST)
    context = {
        'form':form
    }
    return render(request, 'adicionar_semestre.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/semestre')
        return redirect('/login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login')
