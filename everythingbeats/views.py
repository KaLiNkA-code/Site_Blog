from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def main_everythingbeats(request):
    return render(request, 'everythingbeats/everythingbeats.html')


def signupuser(request):
    return render(request, 'everythingbeats/signupuser.html', {'form': UserCreationForm()})
    # if requst.method == 'GET':
    #     return render(request, 'everythingbeats/signupuser.html', {'form': UserCreationForm()})
    # else:
    #     User.objects.create_user(requst.POST[])