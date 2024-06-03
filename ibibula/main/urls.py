
from django.urls import  path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('service/<slug:service_slug>/', views.service, name='service'),
]