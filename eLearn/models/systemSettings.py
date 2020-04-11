from django.db import models

class SystemSettings(models.Model):
	"""docstring for SystemSettings, Mail setting and others"""
	key = models.CharField(max_length = 200)
	value = models.CharField(max_length = 200)
