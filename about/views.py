from django.shortcuts import render
from home.models import Menu
from .models import Skill


def about(request):
    menu = Menu.objects.all()
    skills = Skill.objects.all()
    return render(request, 'about/about.html', {'menu': menu, 'skills': skills})
