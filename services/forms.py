from django import forms
from .models import Service, Order

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service']
