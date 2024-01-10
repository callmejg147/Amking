from django.contrib import admin
from .models import Success, Testimonials
# Register your models here.
class Successadmin(admin.ModelAdmin):
    list_display=['clients', 'projects', 'years', 'awards']
admin.site.register(Success, Successadmin)

class Testimonialadmin(admin.ModelAdmin):
    list_display=['name', 'location', 'content', 'image']
admin.site.register(Testimonials, Testimonialadmin)
