from django.shortcuts import render
from home.models import Menu
from .models import Project


def portfolio(request):
    menu = Menu.objects.all()
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'menu': menu, 'projects': projects})
