from django.db import models

# Create your models here.

#Creating our first model
class Countries(models.Model):
    name= models.CharField(max_length=50,blank=False,default='')
    capital= models.CharField(max_length=50,blank=False,default='')

    class Meta:
        ordering=('id',)