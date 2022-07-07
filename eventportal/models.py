from distutils.command.upload import upload
from djongo import models

# Create your models here.

class Fest(models.Model):
    fest_name = models.CharField(max_length=255)
    fest_venue = models.CharField(max_length=255)
    fest_img = models.ImageField(null=True,blank=True,upload_to="images/")


