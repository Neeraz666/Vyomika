from django.db import models

# Create your models here.
class Contact(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=55)
    email = models.EmailField(default='', max_length=55)
    comment = models.TextField(default='')

    def __str__(self):
        self.name+"'s Comment"