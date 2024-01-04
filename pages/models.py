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

class Testimonials(models.Model):
    name = models.CharField(max_length=100,null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='testimonials/images/', null=True)
    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Testimonials'
