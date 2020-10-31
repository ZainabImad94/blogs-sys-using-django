from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':  # if the form has been submitted
        form = RegistrationForm(request.POST)  # form bound with post data
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=raw_password)
            messages.success(request, 'Account created for {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})
