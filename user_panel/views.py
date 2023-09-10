from django.shortcuts import render, redirect
from .models import Order
from .forms import UserProfileForm
from django.contrib import messages


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login_url')  # Burada 'login_url' kısmını kendi giriş URL'nizle değiştirin.
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'user_panel/dashboard.html', {'orders': user_orders})

def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiliniz güncellendi.')
            return redirect('user_dashboard')
    else:
        form = UserProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'user_panel/profile.html', context)