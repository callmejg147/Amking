"""
URL configuration for amking_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pages.views import home_view, about_view, testimonial_view, services_view
from amking_projects.views import project_view, project_details
from gallery.views import gallery_view


urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('',home_view, name='home'),
    path('about_us/', about_view, name='about'),
    path('projects/', project_view, name='projects'),
    path('project_detail/<str:name>', project_details),
    path('gallery/', gallery_view, name='gallery'),
    path('services', services_view, name='services'),
    path('testimonials/', testimonial_view , name='testimonial'),
    path('admin/', admin.site.urls),
] 
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()