from django.shortcuts import render
from .models import Experience, Education

# Create your views here.

def about(request):
    
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    
    template_name = "about/about.html"
    
    context = {
        'experiences' : experiences,
        'educations'  : educations
    }
    
    return render(request, template_name, context) 