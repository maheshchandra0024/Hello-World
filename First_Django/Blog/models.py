from django.db import models

# Create your models here.
class Bandi(models.Model):
	Year=models.CharField(max_length=60)
	Make=models.CharField(max_length=60)
	Model=models.CharField(max_length=60)
    