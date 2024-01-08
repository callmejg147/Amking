from django.shortcuts import render

from .models import Category, Gallery, GalleryVid
# Create your views here.


def gallery_view(request, *args, **kwargs):
    cat = Category.objects.all()
    gal = Gallery.objects.all().order_by('-id')
    vid = GalleryVid.objects.all().order_by('-id')
    context = {
        'category': cat,
        'images': gal,
        'videos':vid,
    }
    return render(request, 'gallery.html', context=context)
