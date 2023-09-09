from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ServiceForm, OrderForm
from django.contrib import messages
from .models import Service

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ana sayfaya yönlendirme
    else:
        form = ServiceForm()

    context = {'form': form}
    return render(request, 'services/add_service.html', context)

def list_services(request):
    services = Service.objects.all()
    return render(request, 'services/list_services.html', {'services': services})

@login_required
def order_service(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            
            messages.success(request, 'Ordered!')
            return redirect('home')  # redirect to services list after order
    else:
        form = OrderForm()
    return render(request, 'services/order_service.html', {'form': form})