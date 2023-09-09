from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_service, name='add_service'),
    path('list/', views.list_services, name='list_services'),
]
