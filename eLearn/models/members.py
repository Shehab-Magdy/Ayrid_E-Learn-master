from django.db import models

class Members(models.Model):
	"""docstring for members, data of organizations cooperates with us."""
	FullName = models.CharField(max_length = 60)
	description = models.TextField(null = True)
	pic = models.FileField(upload_to = 'uploads/membersPhoto/%Y/%m/%d/')
	status = models.BooleanField(default = True)
