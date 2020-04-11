from django.db import models


class Registration(models.Model):
    
    """docstring for registration, registration info."""
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=30)
    fullName = models.CharField(max_length=60)
    birthDate = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)
    activeUser = models.BooleanField(default=0)
    # file will be saved to MEDIA_ROOT/uploads/regphoto/2015/01/30
    Profilephoto = models.FileField(upload_to='uploads/regPhotos/%Y/%m/%d/')
    creationDate = models.DateField(auto_now_add=True)
    lastModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.email
