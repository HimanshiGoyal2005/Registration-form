# tablesapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('', views.home, name='home'),  # Root URL
    path('registrations/', views.registration_list, name='registration_list'),
    path('registrations/update/<int:pk>/', views.update_registration, name='update_registration'),
    path('delete/<int:id>/', views.delete_registration, name='delete_registration'),
]
