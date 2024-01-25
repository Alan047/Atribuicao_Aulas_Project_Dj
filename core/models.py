from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone





class Curso(models.Model):
    curso = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.curso
    
class Disciplina(models.Model):
    diciplina = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, verbose_name='curso', on_delete=models.CASCADE, null=True ,blank=True)
    periodo = models.IntegerField(blank=True, null=True)
    impar_par = models.CharField(max_length=6, blank=True)

    def save(self, *args, **kwargs):
        if self.periodo % 2 == 0:
            self.impar_par = 'par'
            print('É par')
        else:
            self.impar_par = 'impar'
            print('É impar')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.diciplina
    
class Status(models.Model):
    status = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.status
    
class Semestre(models.Model):
    semestre = models.CharField( max_length=50)
    cursos = models.ManyToManyField(Curso, verbose_name="curso", blank=True)
    status = models.ForeignKey(Status, verbose_name='status', on_delete=models.SET_NULL, null=True, blank=True)
    date_create = models.DateTimeField(default=timezone.now)
    disciplinas = models.ManyToManyField(Disciplina, verbose_name='disciplina', blank=True)
    # par_or_impar = mode


    def __str__(self) -> str:
        return self.semestre
    
class Professor(models.Model):

    NIVELGRADUACAO = [
        ('Graduação', 'Graduação'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
    ]

    professor = models.OneToOneField(User, verbose_name='professor', on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina, verbose_name='disciplinas')
    tempo_exercicio = models.DateField(blank=True, null=True)
    nivel_graduacao = models.CharField(max_length=50, choices=NIVELGRADUACAO, default='Graduação', blank=True, null=True)
    area = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self) -> str:
        return self.professor.username
    
    

