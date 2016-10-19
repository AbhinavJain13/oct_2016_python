from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import User



def index(request):
    return render(request, 'login_reg_app/index.html')

def login(request):
    if request.method == 'POST':
        valid = User.objects.login(request.POST)

        if valid[0] == False:
            print_messages(request, valid[1])
            return redirect('users:login')

        else:
            return success(request, valid[1])

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.ERROR, message)

def success(request, user):
    request.session['user'] = {
        'id' : user.id,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'email' : user.email,
    }
    return render(request, 'login_reg_app/success.html')

def register(request):
    if request.method == 'POST':

        valid = User.objects.register(request.POST)

        if valid[0] == False:
            print_messages(request, valid[1])
            return redirect('users:index')

        else:
             return success(request, valid[1])
