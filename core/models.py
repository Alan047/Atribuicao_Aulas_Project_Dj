from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Disciplina(models.Model):
    diciplina = models.CharField(max_length=50)
    periodo = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.diciplina

class Curso(models.Model):
    curso = models.CharField(max_length=50)
    disciplina = models.ManyToManyField(Disciplina, verbose_name='disciolina')
    
    def __str__(self) -> str:
        return self.curso
    
class Status(models.Model):
    status = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.status
    
class Semestre(models.Model):
    semestre = models.CharField( max_length=50)
    curso_semestre = models.ManyToManyField(Curso, verbose_name="curso", blank=True, null=True)
    status = models.ForeignKey(Status, verbose_name='status', on_delete=models.SET_NULL, null=True, blank=True)
    date_create = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.semestre
    
class Professor(models.Model):
    professor = models.OneToOneField(User, verbose_name='professor', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.professor.username
    
    

