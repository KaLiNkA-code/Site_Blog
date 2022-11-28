from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
import random
import smtplib
count_orders = 100


def home(request):
    return render(request, 'everythingbeats/home.html')


def main_everythingbeats(request):
    return render(request, 'everythingbeats/everythingbeats.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'everythingbeats/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'everythingbeats/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('main_everythingbeats')

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')



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




def password(request):
    global count_orders
    price = 0
    order = ""
    text = "Нету"
    contacts = ""

    if request.GET.get('text'):
        text = request.GET.get('text')
    if request.GET.get('tg'):
        contacts = request.GET.get('tg')
        
    if request.GET.get('beat'):
        price += 490
        order += "| Бит |"
    if request.GET.get('studio'):
        price += 1490
        order += "| Студия |"
    if request.GET.get('mix'):
        price += 840
        order += "| Сведение |"
    if request.GET.get('Upload'):
        price += 990
        order += "| Выгрузка на площадки |"

    
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login("findek.official@gmail.com", "saskcwbuwukgcyrl")
    # кодировка письма
    charset = 'Content-Type: text/plain; charset=utf-8'
    mime = 'MIME-Version: 1.0'
    text_t = f"Привет! Цена заказа:{price}\n делали: {order}\n пожелание: {text} \n Контакт: {contacts}"
    body = "\r\n".join((f"From: findek.official@gmail.com", f"To: findek.official@gmail.com",
                        f"Subject: Новый заказ под номером {count_orders}", mime, charset, "", text_t))
    smtpObj.sendmail("justkiddingboat@gmail.com", "findek.official@gmail.com", body.encode('utf-8'))
    count_orders += 1
    smtpObj.quit()

    return render(request, 'everythingbeats/order.html', {'price': price, 'text': text, 'order': order, 'contacts': contacts})
