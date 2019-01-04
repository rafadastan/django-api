from django.db import models

class Operacao(models.Model):
        
	titulo = models.CharField('titulo do video', max_length=50)
	duracao = models.DurationField(help_text="Use format: <em>11:11:11</em>.")
	nome_arquivo = models.CharField(max_length=50)
	video = models.FileField(upload_to='uploads/', default='')

	def __str__(self):
		return self.titulo
	

class Upload(models.Model):
	    
	startime = models.TimeField(help_text="Please use the following format: <em>11:11:11</em>.")
	endtime = models.TimeField(help_text="Please use the following format: <em>11:11:11</em>.")
	nome = models.CharField('nome do arquivo',max_length=50)
	file = models.FileField('arquivo txt', upload_to='uploads/', default='')

	def __str__(self):
		return self.nome

