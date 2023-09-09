from django.shortcuts import render, redirect
from .forms import ServiceForm
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
