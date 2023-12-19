from django.shortcuts import render

from .models import Category, Gallery
# Create your views here.


def gallery_view(request, *args, **kwargs):
    cat = Category.objects.all()
    gal = Gallery.objects.all().order_by('-id')
    context = {
        'category': cat,
        'images': gal,
    }
    return render(request, 'gallery.html', context=context)
