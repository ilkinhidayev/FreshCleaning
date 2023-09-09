from django.contrib import admin
from .models import Profile

# Profile için admin modelini tanımlayalım
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']  # Admin panelinde görüntülemek istediğiniz alanları belirtin.
    search_fields = ['user__username', 'bio']  # Arama yapılacak alanları belirtin.

# Modeli admin paneline kaydedin.
admin.site.register(Profile, ProfileAdmin)