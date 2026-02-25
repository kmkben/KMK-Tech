from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Example: You can send an email or store it in DB
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            email_subject = f"KMK IOTech Contact — {subject}"
            
            email_body = f"""
New message KMK IOTech from :

Name: {name}
Email: {email}

Message: 
{message}
"""
            
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email='kemokokeita710@gmail.com', #settings.DEFAULT_FROM_EMAIL
                to=["kemoko.keita@outlook.com"],  # ← YOUR OUTLOOK
                reply_to=[email],  # VERY IMPORTANT ⭐
            )

            email_message.send(fail_silently=False)

            # Here we use Django messages framework to show success
            messages.success(request, "✅ Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    
    template_name = "contact/contact.html"
    
    context = {
        'form' : form
    }
    
    return render(request, template_name, context)