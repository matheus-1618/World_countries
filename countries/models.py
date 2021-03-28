from django.db import models

# Create your models here.

#Creating our first model
class Countries(models.Model):
    name= models.CharField(max_length=50,blank=False,default='')
    capital= models.CharField(max_length=50,blank=False,default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering=('id',)