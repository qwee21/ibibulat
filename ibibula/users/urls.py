
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('edituser/', views.edituser, name='edituser'),
    path('editservice/', views.editservice, name='editservice'),
    path('logout/', views.logout, name='logout'),
]