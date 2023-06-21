from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Visualize(models.Model):
    snum = models.AutoField(primary_key=True)
    data = ArrayField(models.CharField(max_length=100))
    names = ArrayField(models.CharField(max_length=255))