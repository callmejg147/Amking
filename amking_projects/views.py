from django.shortcuts import render

from .models import Projects

# Create your views here.


def project_view(request, *args, **kwargs):
    prj = Projects.objects.all().order_by('-id')
    context = {
        'projects': prj,
    }
    return render(request, 'projects.html', context=context)



def project_details(request, name):

    projs = Projects.objects.all().order_by('-id')
    for proj in projs:
        print(name)

        if name == proj.title:
            context = {
                'project': proj,
            }
            return render(request, 'project_detail.html', context=context)