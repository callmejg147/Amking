from django.contrib import admin
from .models import Category, Gallery
# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category, Categoryadmin)

class Galleryadmin(admin.ModelAdmin):
    list_display=['title', 'category', 'image']
admin.site.register(Gallery, Galleryadmin)
