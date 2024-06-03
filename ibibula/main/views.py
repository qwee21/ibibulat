from django.shortcuts import render, get_object_or_404
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

def service(request, service_slug):
    service = get_object_or_404(Services, slug=service_slug)

    context = {
        'name': service.name,
        'service': service,
    }
    return render(request, 'main/service.html', context)
