from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, primary_key=True)
    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Category'



class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='images/')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Gallery'