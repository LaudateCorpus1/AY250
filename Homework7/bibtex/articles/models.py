from django.db import models
from django import forms

class Collection(models.Model):
    name = models.CharField(max_length=70)

    def __unicode__(self):
        return self.name

class Article(models.Model):
	author_list = models.CharField(max_length=150)
	journal     = models.CharField(max_length=100)
	volume      = models.IntegerField()
	pages       = models.CharField(max_length=25)
	year        = models.IntegerField()
	title       = models.CharField(max_length=400)
	
	collection  = models.ForeignKey(Collection)
	
	def __unicode__(self):
		return self.title