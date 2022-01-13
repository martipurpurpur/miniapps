from django.db import models

# Create your models here.
class Sheduler(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=250, unique=True)
    time = models.CharField(max_length=250)
    shedule = models.TextField()

