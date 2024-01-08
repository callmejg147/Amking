from django.contrib import admin
from .models import Category, Gallery, GalleryVid
# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category, Categoryadmin)

class Galleryadmin(admin.ModelAdmin):
    list_display=['title', 'image']
admin.site.register(Gallery, Galleryadmin)

class GalleryVidadmin(admin.ModelAdmin):
    list_display=['title', 'video']
admin.site.register(GalleryVid, GalleryVidadmin)
