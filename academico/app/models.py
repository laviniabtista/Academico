from django.db import models

# Create your models here.
class Ocupacao(models.Model):
    nome_ocupacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_ocupacao
    
class Cidades(models.Model):
    nome_cidade = models.CharField(max_length=100)
    UF_cidade = models.CharField(max_length=2)

    def __str__(self):
        return self.nome_cidade
    
class Pessoas(models.Model):
    nome_pessoa = models.CharField(max_length=100)
    pai_pessoa = models.CharField(max_length=100)
    mae_pessoa = models.CharField(max_length=100)
    cpf_pessoa = models.CharField(max_length=100)
    data_nasc = models.DateField()
    email_pessoa = models.CharField(max_length=100)
    cidade_pessoa = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    ocupacao_pessoa = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_pessoa
    
    
class Instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=100)
    site_instituicao = models.CharField(max_length=100)
    telefone_instituicao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_instituicao    
        
class AreasConhecimento(models.Model):
    nome_areas = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_areas
        
class Cursos(models.Model):
    nome_curso = models.CharField(max_length=100)
    cargaHoraria_curso = models.CharField(max_length=100)
    duracaoMeses_curso = models.CharField(max_length=100)
    areaSaber_curso = models.ForeignKey(AreasConhecimento, on_delete=models.CASCADE)
    instituicao_curso = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_curso
            
class Periodos(models.Model):
    periodo = models.CharField(max_length=100)
    def __str__(self):
        return self.periodo
            
class Disciplinas(models.Model):
    nome_disciplina = models.CharField(max_length=100)
    areaSaber_disciplina = models.ForeignKey(AreasConhecimento, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome_disciplina
            
class Matricula(models.Model):
    instituicao_matricula = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso_matricula = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    pessoa_matricula = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    dataInicio_matricula = models.DateField()
    dataTermino_matricula = models.DateField()

    def __str__(self):
        return f'{self.instituicao_matricula}'
            
class TiposAvaliacao(models.Model):
    nome_tipoAvaliacao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_tipoAvaliacao
            
class Avaliacoes(models.Model):
    descricao_avaliacao = models.CharField(max_length=1000)
    curso_avaliacao = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina_avaliacao = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    tipo_avaliacao = models.ForeignKey(TiposAvaliacao, on_delete=models.CASCADE)
    instituicao_curso = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao_avaliacao
            
class Frequencia(models.Model):
    curso_frequencia = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina_frequencia = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    numFaltas_frequencia = models.CharField(max_length=100)
    

    def __str__(self):
        return self.numFaltas_frequencia
            
class Turmas(models.Model):
    nome_turma = models.CharField(max_length=100)
    periodoSem_turma = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_turma
            

            
class Ocorrencias(models.Model):
    descricao_ocorrencia = models.CharField(max_length=1000)
    data_ocorrencia = models.DateField()
    curso_ocorrencia = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina_ocorrencia = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    pessoa_ocorrencia = models.ForeignKey(Pessoas, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao_ocorrencia
            
class DisciplinasCurso(models.Model):
    nome_disciplinaCurso = models.CharField(max_length=100)
    cargaHoraria_disciplinaCurso = models.CharField(max_length=100)
    curso_disciplinaCurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    periodo_disciplinaCurso = models.ForeignKey(Periodos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_disciplinaCurso
