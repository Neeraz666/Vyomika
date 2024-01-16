from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Student(models.Model):
    std_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete = models.CASCADE)
    stdname = models.CharField(default='', max_length=55)
    stdemail = models.CharField(default='', max_length=100)
    stdadd = models.CharField(default='', max_length=255)
    stdphone = models.CharField(default='', max_length=10)
    stdfaculty = models.CharField(default='', max_length=55)
    stdgender = models.CharField(default='', max_length=6)
    stdimage = models.ImageField(default='', upload_to='stdimg')

    def __str__(self):
        return self.stdname+' Id: '+str(self.std_id)
    
class Staff(models.Model):
    stf_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete = models.CASCADE)
    stfname = models.CharField(default='', max_length=55)
    stfemail = models.CharField(default='', max_length=100)
    stfadd = models.CharField(default='', max_length=255)
    stfphone = models.CharField(default='', max_length=10)
    stfrole = models.CharField(default='', max_length=55)
    stfgender = models.CharField(default='', max_length=6)
    stfimage = models.ImageField(default='', upload_to='stdimg')

    def __str__(self):
        return self.stfname+' Id: '+str(self.stf_id)
    
    