from django.shortcuts import render
from .models import Semestre, Professor

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
    return render(request, 'professores.html', {'professor':professor})

def select_semestre(request, id):
    semestre = Semestre.objects.get(pk=id)
    context = {
        'semestre' : semestre
    }
    return render(request, 'select_semestre.html', context)

