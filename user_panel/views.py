from django.shortcuts import render, redirect
from .models import Order

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login_url')  # Burada 'login_url' kısmını kendi giriş URL'nizle değiştirin.
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'user_panel/dashboard.html', {'orders': user_orders})
