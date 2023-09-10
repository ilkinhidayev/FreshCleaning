from django.contrib import admin
from django.urls import path, include
from accounts import views
from user_panel import views as user_panel_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('services/', include('services.urls')),
    path('dashboard/', include('user_panel.urls')),  # user_panel uygulamasını dahil ettik.
]
