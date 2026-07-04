from django.shortcuts import render
from .models import Project, Contact

def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def contact(request):
    success = False
    error = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and subject and message:
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            success = True
        else:
            error = True
    return render(request, 'portfolio/contact.html', {'success': success, 'error': error})