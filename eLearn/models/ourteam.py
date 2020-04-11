from django.db import models

class ourTeam(models.Model):
	"""docstring for ourTeam, Ayrid team members"""
	FullName = models.CharField(max_length = 60)
	description = models.TextField(null = True)
	JobTitle = models.CharField(max_length = 60)
	pic = models.FileField(upload_to = 'uploads/ourTeam/%Y/%m/%d/')
	status = models.BooleanField(default = True)
