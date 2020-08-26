from django.db import models


class Contacts(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	message = models.TextField()
	def __str__(self):
		return self.name	
