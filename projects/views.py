from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def project_list(request):
    
    template_name = 'projects/projects_list.html'
    
    projects = Project.objects.all()
    
    context = {
        'projects' : projects
    }
    
    return render(request, template_name, context)



def project_show(request, slug):
    
    template_name = 'projects/projects_show.html'
    
    project = get_object_or_404(Project, slug=slug)
    
    context = {
        'project' : project
    }
    
    return render(request, template_name, context)
