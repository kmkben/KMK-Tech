from django.shortcuts import render
from projects.models import Project

# Create your views here.

def home(request):
    
    template_name = 'home/home.html'
    
    latest_projects = Project.objects.order_by('-created_at')[:2]
    
    context = {
        'latest_projects' : latest_projects
    }
    return render(request, template_name, context)
