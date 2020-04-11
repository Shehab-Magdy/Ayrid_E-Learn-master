from django.db import models


class Events(models.Model):
    """docstring for events, collecting events data"""
    name = models.CharField(max_length=60)
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=60)
    contactPhone = models.CharField(max_length=60)
    description = models.TextField(null=True)
    pic = models.FileField(upload_to='uploads/events/%Y/%m/%d/')
    eventStatus = models.BooleanField(default=True)

    def __str__(self):
        return self.name
