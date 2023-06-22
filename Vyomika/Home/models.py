from django.db import models

# Create your models here.
class Contact(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55, default='')
    email = models.CharField(max_length=55, default='',)
    comment = models.TextField()

    def __str__(self):
        return self.name+"'s Comment"