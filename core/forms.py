from django.forms import ModelForm
from .models import Semestre

class SemestreForm(ModelForm):
    class Meta:
        model = Semestre
        fields = ['semestre', 'cursos','disciplinas']