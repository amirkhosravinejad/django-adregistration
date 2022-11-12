from django.db import models

# Create your models here.
class advertise(models.Model):

    title = models.CharField(max_length=100)
    seller = models.CharField(max_length=100)
    email = models.EmailField()
    #photo = models.ImageField()