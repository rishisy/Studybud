from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
   
   
    class Meta:
        ordering=['completed']

  
class UploadImage(models.Model):     
    poster=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    keywords = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='static/upload')  
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):  
        return self.caption
