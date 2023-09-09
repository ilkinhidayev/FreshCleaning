from django.urls import path
from . import views
from .views import profile, change_password

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('change-password/', change_password, name='change-password'),
]