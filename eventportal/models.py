from distutils.command.upload import upload
from email.policy import default
from signal import default_int_handler
from djongo import models

# Create your models here.

class Fest(models.Model):
    fest_name = models.CharField(max_length=255,default="")
    fest_venue = models.CharField(max_length=255,default="")
    fest_img = models.ImageField(null=True,blank=True,upload_to="images/")
    fest_desc = models.TextField(default="")

class Events(models.Model):
    event_name = models.CharField(max_length=255)
    event_img = models.ImageField(null=True,blank=True,upload_to="images/eventimg")
    event_tags = models.CharField(max_length=255)
    event_desc = models.TextField(default="")
    event_fest = models.ForeignKey("Fest", on_delete=models.CASCADE)
    objects = models.DjongoManager()

