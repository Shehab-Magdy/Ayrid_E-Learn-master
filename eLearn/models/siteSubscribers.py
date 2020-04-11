from django.db import models

class SiteSubscribers(models.Model):
	"""docstring for SiteSubscribers, collecting subscribers emails"""
	email = models.EmailField(max_length = 254)
	status = models.BooleanField(default = True)
