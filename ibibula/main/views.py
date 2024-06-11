from django.shortcuts import render, get_object_or_404
from .models import Services, Categories, Subcategories



def index(request):
    services = Services.objects.select_related('category', 'subcategory').prefetch_related('performer_set__user').all()
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
    performer = service.performer_set.first()  # Assuming each service has one performer for simplicity

    context = {
        'service': service,
        'performer': performer,
    }
    return render(request, 'main/service.html', context)

