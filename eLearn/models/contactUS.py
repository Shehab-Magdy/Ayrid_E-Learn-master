from django.db import models

class ContactUS(models.Model):
	"""docstring for ContactUS, visitors messages throw contact us page"""
	firstName = models.CharField(max_length = 60)
	lastName = models.CharField(max_length = 60)
	email = models.EmailField(max_length = 254)
	message = models.TextField(null = True)
	replyStatus = models.BooleanField(default = True)
