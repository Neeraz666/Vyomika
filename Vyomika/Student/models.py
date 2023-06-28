from django.db import models

# Create your models here.
class Student(models.Model):
    std_id = models.AutoField(primary_key=True)
    stdname = models.CharField(default='', max_length=55)
    stdemail = models.CharField(default='', max_length=100)
    stdadd = models.CharField(default='', max_length=255)
    stdphone = models.CharField(default='', max_length=10)
    stdfaculty = models.CharField(default='', max_length=55)
    stdgender = models.CharField(default='', max_length=6)
    stdimage = models.ImageField(default='', upload_to='stdimg')

    def __str__(self):
        return self.stdname+' Id: '+str(self.std_id)
    
    