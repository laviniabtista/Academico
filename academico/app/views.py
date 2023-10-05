from django.shortcuts import render
from . models import *
# Create your views here.

def AreaConhecimento(request):
    areas = {
        'areas' :AreasConhecimento.objects.all()
    }
    return render(request, 'AreasConhecimento/areas.html', areas)

def Avaliacao(request):
    avaliacoes = {
        'avaliacoes' :Avaliacoes.objects.all()
    }
    return render(request, 'Avaliacoes/avaliacoes.html', avaliacoes)

def Cidade(request):
    cidades = {
        'cidades' :Cidades.objects.all()
    }
    return render(request, 'Cidades/cidades.html', cidades)

def Curso(request):
    cursos = {
        'cursos' :Cursos.objects.all()
    }
    return render(request, 'Cursos/cursos.html', cursos)

def Disciplina(request):
    disciplinas = {
        'disciplinas' :Disciplinas.objects.all()
    }
    return render(request, 'Disciplinas/disciplinas.html', disciplinas)


def DisciplinaCurso(request):
    disciplinasCurso = {
        'disciplinasCurso' :DisciplinasCurso.objects.all()
    }
    return render(request, 'DisciplinasCursos/disciplinasCurso.html', disciplinasCurso)

def Frequencias(request):
    frequencias = {
        'frequencias' :Frequencia.objects.all()
    }
    return render(request, 'Frequencia/frequencias.html', frequencias)

def Instituicoes(request):
    instituicoes = {
        'instituicoes' :Instituicao.objects.all()
    }
    return render(request, 'Instituicoes/instituicoes.html', instituicoes)

def Matriculas(request):
    matriculas = {
        'matriculas' :Matricula.objects.all()
    }
    return render(request, 'Matriculas/matriculas.html', matriculas)

def Ocorrencia(request):
    ocorrencias = {
        'ocorrencias' :Ocorrencias.objects.all()
    }
    return render(request, 'Ocorrencias/ocorrencias.html', ocorrencias)

def Ocupacoes(request):
    ocupacoes = {
        'ocupacoes' :Ocupacao.objects.all()
    }
    return render(request, 'Ocupacoes/ocupacoes.html', ocupacoes)

def Periodo(request):
    periodos = {
        'periodos' :Periodos.objects.all()
    }
    return render(request, 'Periodos/periodos.html', periodos)

def Pessoa(request):
    pessoas = {
        'pessoas' :Pessoas.objects.all()
    }
    return render(request, 'Pessoas/pessoas.html', pessoas)

def TipoAvaliacao(request):
    tipos_avaliacoes = {
        'tipos_avaliacoes' :TiposAvaliacao.objects.all()
    }
    return render(request, 'TiposAvaliacao/tipos avaliacoes.html', tipos_avaliacoes)

def Turma(request):
    turmas = {
        'turmas' :Turmas.objects.all()
    }
    return render(request, 'Turmas/turma.html', turmas)
