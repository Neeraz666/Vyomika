from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Visualize(models.Model):
    snum = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, default = None, null=True, blank=True)
    fname = models.CharField(max_length=55, default='')
    datas = models.CharField(max_length=100, default='')
    names = models.CharField(max_length=255, default='')
    graph = models.ImageField(default='', upload_to='graphs')

    def __str__(self):
        return self.fname+"'s Data" 
    

class FileVisualize(models.Model):
    num = models.AutoField(primary_key=True)
    file = models.FileField(default='', upload_to='files')
    graph = models.ImageField(default='', upload_to='file/graphs')
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, default = None, null=True, blank=True)

    def __str__(self):
        return self.user+'s file'
