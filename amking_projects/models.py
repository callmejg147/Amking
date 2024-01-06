from django.db import models

# Create your models here.
class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 100, null=False)
    short_description = models.TextField(max_length=350, null=False, default='none')
    description = models.TextField(null=False)
    img1 = models.ImageField(upload_to='project/images/',blank=True,null=True)
    img2 = models.ImageField(upload_to='project/images/',blank=True,null=True)
    img3 = models.ImageField(upload_to='project/images/',blank=True,null=True)
    img4 = models.ImageField(upload_to='project/images/',blank=True,null=True)
    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Projects'
