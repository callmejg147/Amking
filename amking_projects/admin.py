from django.contrib import admin
from .models import Projects

# Register your models here.
class Projectadmin(admin.ModelAdmin):
    list_display=['title', 'short_description', 'description', 'img1', 'img2', 'img3', 'img4']
admin.site.register(Projects)
