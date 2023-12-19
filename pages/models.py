from django.db import models


# Create your models here.

class Success(models.Model):
    clients = models.IntegerField()
    projects = models.IntegerField()
    years = models.IntegerField()
    awards = models.IntegerField()
    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Success'