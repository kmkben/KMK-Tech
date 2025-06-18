from django.shortcuts import render

# Create your views here.

def contact(request):
    
    template_name = "contact/contact.html"
    
    return render(request, template_name)