"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('semestre/', views.semestre, name='semestre'),
    path('professores/', views.professores, name='professores'),
    path('semestre/select=<int:id>', views.select_semestre, name='select_semestre'),
    path('curso/', views.cursos_list_page, name='cursos'),
    path('dicliplinas/<int:id2>/<int:id>', views.disciplinas_list, name='disciplinas'),

    #adicionar 
     path('adicionar_semestre/', views.adicionar_semestre, name='addSemestre'),

     #usuário
     path('login/', views.login_view, name='login'),


]
