from __future__ import unicode_literals
#from tinymce import models as tinymce_models
from django.db import models


class Comentario(models.Model):
	id = models.AutoField(primary_key = True)
	comentario = models.TextField()
	date = models.DateField(auto_now = False, auto_now_add = True)
	nombre = models.CharField(max_length = 200)
	email = models.EmailField()

	def __unicode__(self):
		return self.comentario

class Post(models.Model):
	id = models.AutoField(primary_key = True)
	#comentarios = models.ManyToManyField(Comentario)
	nueva_entrada = models.TextField()
	descripcion = models.TextField()
	titulo = models.CharField(max_length = 255)	
	categoria = models.CharField(max_length = 255)
	fecha = models.DateField(auto_now=False, auto_now_add=False)
	firma = models.CharField(max_length = 200)
	imagen = models.URLField(null = True)
	

	def __unicode__(self):
		return self.titulo
