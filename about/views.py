from django.shortcuts import render
from home.models import Menu


def about(request):
    menu = Menu.objects.all()
    return render(request, 'about/about.html', {'menu': menu})
