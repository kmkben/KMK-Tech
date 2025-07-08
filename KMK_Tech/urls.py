"""
URL configuration for KMK_Tech project.

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
from django.urls import path

import core.views
import contact.views
import about.views
import projects.views

urlpatterns = [
    path('', core.views.home, name='home'),
    
    path('projects/', projects.views.project_list, name='projects'),
    path('projects/<slug:slug>/', projects.views.project_show, name='project_show'),
    
    path('contact/', contact.views.contact, name='contact'),
    path('about/', about.views.about, name='about'),
    
    path('admin/', admin.site.urls),
]
