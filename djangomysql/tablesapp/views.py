# tablesapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, Registration


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def update_registration(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'update_registration.html', {'form': form})


def delete_registration(request, id):
    registration = get_object_or_404(Registration, id=id)
    if request.method == 'POST':
        registration.delete()
        return redirect('registration_list')  # Redirect to the list view after deletion
    return render(request, 'delete_registration.html', {'registration': registration})


def success(request):
    return render(request, 'success.html')


def home(request):
    return render(request, 'home.html')


def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'registration_list.html', {'registrations': registrations})
