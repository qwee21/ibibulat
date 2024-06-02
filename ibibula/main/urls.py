
from django.urls import include, path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
]