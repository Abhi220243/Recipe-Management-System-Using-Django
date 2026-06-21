from django.db import models

# Create your models here.

class recipie_model(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.TextField()
    steps=models.TextField()
    image=models.ImageField(upload_to='recipie')