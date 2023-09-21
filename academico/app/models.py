from django.db import models

# Create your models here.
class Ocupacao(models.Model):
  nomeOcup = models.CharField(max_length=100)
  def _str_(self):
       return f"{self.nomeOcup}"
  
class Instituicao(models.Model):
   nomeInst = models.CharField(max_length=100)
   site = models.CharField(max_length=100)
   telefone = models.CharField(max_length=11, unique=True)
   def _str_(self):
     return f"{self.nomeInst}, {self.site},{self.telefone}"

class Areas(models.Model):
   nomeSaber = models.CharField(max_length=100)
   def _str_(self):
     return f"{self.nomeSaber}"
   
class Cidade(models.Model):
   nome_Cidade = models.CharField(max_length=100)
   UF = models.CharField(max_length=100)
   def _str_(self):
     return f"{self.nome_Cidade}, {self.UF} "

class Tipos_Avaliacao(models.Model):
   nome_Avaliacao = models.CharField(max_length=100)
   def _str_(self):
     return f"{self.nome_Avaliacao}"

class Pessoa(models.Model):
   nome = models.CharField(max_length=100)
   pai = models.CharField(max_length=100)
   mae = models.CharField(max_length=100)
   cpf = models.CharField(max_length=11, unique=True)
   data_nasc = models.DateField()
   email = models.CharField(max_length=100)
   cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
   def _str_(self):
     return f"{self.nome}, {self.pai},{self.mae},{self.cpf}, {self.data_nasc}, {self.email} "

class Curso(models.Model):
   nomeCurso = models.CharField(max_length=100)
   carga_horaria_total = models.CharField(max_length=100)
   duracao_meses = models.CharField(max_length=100)
   def _str_(self):
     return f"{self.nomeCurso}, {self.carga_horaria_total},{self.duracao_meses}"

class Semestres(models.Model):
   periodo = models.CharField(max_length=100)
   def _str_(self):
     return f"{self.periodo}"

class Disciplina(models.Model):
   nomeDisci = models.CharField(max_length=100)
   areas_saber = models.ForeignKey(Areas, on_delete=models.CASCADE)
   def _str_(self):
     return f"{self.nomeDisci}, {self.areas_saber}"

class Matricula(models.Model):
   instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
   pessoa_nome = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
   data_Inicio = models.DateField()
   data_previs_termino = models.DateField()
   def _str_(self):
     return f"{self.instituicao}, {self.curso},{self.pessoa}, {self.data_Inicio}, {self.data_previs_termino}"

class Avaliacao(models.Model):
   descricao = models.CharField(max_length=100)
   tipo_avaliacao = models.ForeignKey(Tipos_Avaliacao, on_delete=models.CASCADE)
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
   disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
   def _str_(self):
     return f"{self.descricao}, {self.tipo_avaliacao},{self.Curso}, {self.disciplina}"

class Frequencia(models.Model):
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
   disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
   numero_faltas = models.CharField(max_length=100)
   def _str_(self):
     return f"{self.curso}, {self.disciplina}, {self.numero_faltas} "

class Ocorrencia(models.Model):
   descricao = models.CharField(max_length=100)
   data_Ocorrencia = models.DateField()
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
   disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
   pessoa_nome = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
   def _str_(self):
     return f"{self.descricao}, {self.data_Ocorrencia},{self.curso}, {self.disciplina},{self.pessoa} "

class Disciplina_Curso(models.Model):
   nome_Disci = models.CharField(max_length=100)
   carga_horaria = models.CharField(max_length=100)
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
   periodo = models.ForeignKey(Semestres, on_delete=models.CASCADE)
   def _str_(self):
     return f"{self.nome_Disci}, {self.carga_horaria},{self.curso}, {self.periodo}"

class Turmas(models.Model):
   nome_Turma = models.CharField(max_length=100)
   periodo_semestre = models.CharField(max_length=100)
   def _str_(self):
     return f"{self.nome_Turma}, {self.periodo_semestre}"




