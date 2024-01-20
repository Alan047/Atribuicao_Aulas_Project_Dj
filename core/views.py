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
    cursos = Curso.objects.all()
    disciplinas = Disciplina.objects.all().order_by('curso')
    context = {
        'semestre':semestre,
        'cursos':cursos,
        'disciplinas':disciplinas,
    }
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
    print(id)
    semestre = Semestre.objects.get(pk=id)
    curso = Curso.objects.get(pk=id2)
    disciplinas = curso.disciplina_set.all()
    if request.method == 'POST':
        disciplinas_form = request.POST.getlist('select-addDisciplinas')
        print(f' disc {disciplinas_form}')
        for d in disciplinas_form:
            semestre.disciplinas.add(d)
    context = {
        'disciplinas_semestre': disciplinas.filter(semestre=semestre),
        'disciplinas_curso': Disciplina.objects.exclude(semestre=semestre).filter(curso=curso),
        'curso': curso,
        'semestre' : semestre,
    }
    return render(request, 'disciplinas.html', context)

@login_required(login_url="/login")
def adicionar_semestre(request):
    if request.method == 'POST':
        semestre = request.POST.get('semestre')
        cursos = request.POST.getlist('curso')
        disciplinas_periodo = request.POST.get('select-disciplinas')
        print(disciplinas_periodo)
        novo_semestre = Semestre.objects.create(semestre=semestre)
        for curso in cursos:
            ...
            # curso_object = Curso.objects.get(pk=int(curso))
            # novo_semestre.cursos.add(curso_object)
          
    return redirect('semestre')

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
