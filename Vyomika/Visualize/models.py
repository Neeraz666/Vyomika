from django.db import models


# Create your models here.
class Visualize(models.Model):
    snum = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=55, default='')
    datas = models.CharField(max_length=100, default='')
    names = models.CharField(max_length=255, default='')
    graph = models.ImageField(default='', upload_to='graphs')
    file = models.FileField(default='', upload_to='files')

    def __str__(self):
        return self.fname+"'s Data" 