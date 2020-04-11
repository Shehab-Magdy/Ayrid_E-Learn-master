from django.db import models


class HaederSlider(models.Model):
    """docstring for haeder, images in the slider of the home page"""
    name = models.CharField(max_length=60)
    pic = models.FileField(upload_to='uploads/slider/%Y/%m/%d/')

