# Generated by Django 5.0.1 on 2024-01-17 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_disciplina_impar_par'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='impar_par',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
