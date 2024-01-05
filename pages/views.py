from django.shortcuts import render
from django.http import HttpResponse

# import models:
from gallery.models import Gallery
from pages.models import Success, Testimonials
from amking_projects.models import Projects


# Create your views here.
def home_view(request, *args, **kwargs):
    gal = Gallery.objects.all().order_by('-id')
    success = Success.objects.all()
    projects = Projects.objects.all().order_by('-id')
    testimonials = Testimonials.objects.all()
    context = {
        'gallery': gal,
        'success': success,
        'projects': projects,
        'testimonials': testimonials,
    }
    return render(request,'index.html', context=context)

def about_view(request, *args, **kwargs):
    return render(request, 'about.html',{})

def testimonial_view(request, *args, **kwargs):
    return render(request, 'testimonials.html',{})

def services_view(request, *args, **kwargs):
    return render(request, 'services.html', {})
