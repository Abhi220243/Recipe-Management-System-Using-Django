from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class recipie_model(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.TextField()
    steps=models.TextField()
    image=models.ImageField(upload_to='recipie')