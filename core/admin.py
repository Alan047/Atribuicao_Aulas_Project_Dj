from django.contrib import admin
from .models import Curso, Semestre, Professor, Disciplina, Status

@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'semestre', 'mostrar_cursos', 'mostrar_materias']

    # def mostrar_materias(self, obj):
    #     return ", ".join([materia.materia for materia in obj.materias.all()])
    
    # def mostrar_cursos(self, obj):
    #     return ", ".join([curso.curso for curso in obj.curso.all()])
@admin.register(Curso)  
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Professor, Disciplina, Status)  
class CursoAdmin(admin.ModelAdmin):
    pass

