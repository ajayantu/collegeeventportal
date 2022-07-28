from djongo import models
from django.contrib.auth.models import User
# Create your models here.
import uuid



class Fests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fest_name = models.CharField(max_length=255)
    fest_author = models.ForeignKey(User,on_delete=models.CASCADE)
    fest_venue = models.CharField(max_length=255)
    fest_img = models.ImageField(null=True,blank=True,upload_to="images/")
    fest_desc = models.TextField()
    def __str__(self):
        return self.fest_name+' | '+self.fest_author.username

    
class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_name = models.CharField(max_length=255,default="")
    event_author = models.ForeignKey(User,on_delete=models.CASCADE)
    event_img = models.ImageField(null=True,blank=True,upload_to="images/")
    event_tags = models.CharField(max_length=255,default="")
    event_desc = models.TextField(default="")
    event_fest = models.ForeignKey(Fests, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name+' | '+self.event_author.username
    
class Registered(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

