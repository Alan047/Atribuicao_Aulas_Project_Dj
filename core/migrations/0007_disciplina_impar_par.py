# Generated by Django 5.0.1 on 2024-01-17 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_semestre_cursos_alter_semestre_disciplinas'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='impar_par',
            field=models.CharField(default='impar', max_length=5),
        ),
    ]
