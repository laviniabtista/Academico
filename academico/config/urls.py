"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('AreasConhecimento/', AreaConhecimento, name='areas'),
    path('Avaliacoes/', Avaliacao, name='avaliacoes'),
    path('Cidades/', Cidade, name='cidades'),
    path('Cursos/', Curso, name='cursos'),
    path('Disciplinas/', Disciplina, name='disciplinas'),
    path('DisciplinasCursos/', DisciplinaCurso, name='disciplinasCurso'),
    path('Frequencia/', Frequencias, name='frequencias'),
    path('Instituicoes/', Instituicoes, name='instituicoes'),
    path('Matriculas/', Matriculas, name='matriculas'),
    path('Ocorrencias/', Ocorrencia, name='ocorrencias'),
    path('Ocupacoes/', Ocupacoes, name='ocupacoes'),
    path('Periodos/', Periodo, name='periodos'),
    path('Pessoas/', Pessoa, name='pessoas'),
    path('TiposAvaliacao/', TipoAvaliacao, name='tipos_avaliacoes'),
    path('Turmas/', Turma, name='turmas'),
]
