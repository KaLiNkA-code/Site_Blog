from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login


def main_everythingbeats(request):
    return render(request, 'everythingbeats/everythingbeats.html')


def signupuser(request):
    #  return render(request, 'everythingbeats/signupuser.html', {'form': UserCreationForm()})
    if request.method == 'GET':
        return render(request, 'everythingbeats/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('main_everythingbeats')
            except IntegrityError:
                return render(request, 'everythingbeats/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already taken. Please choose a new one.'})
        else:
            return render(request, 'everythingbeats/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})
