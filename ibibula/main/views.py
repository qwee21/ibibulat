from django.shortcuts import render
from .models import Services, Categories, Subcategories

def index(request):
    services = Services.objects.all()
    categories = Categories.objects.all()
    subcategories = Subcategories.objects.all()

    context = {
        'title': 'Всё для студентов!',
        'services': services,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'main/index.html', context)

def service(request):
    services = Services.objects.all()

    context = {
        'name': 'Имя исполнителя',
        'services': services,
    }
    return render(request, 'main/service.html', context)
