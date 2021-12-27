from django.db import models

# Create your models here.
class MiniApp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()