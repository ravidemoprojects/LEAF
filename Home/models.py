from django.db import models

# Create your models here.
class User(models.Model):
    url = models.URLField(max_length=5000)
    max_price = models.IntegerField()
    min_price = models.IntegerField()

