from django.contrib import admin
from .models import Curso, Semestre, Professor, Disciplina, Status
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    pass
   
@admin.register(Curso)  
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Professor, Disciplina, Status)  
class CursoAdmin(admin.ModelAdmin):
    pass





