from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .models import Quiz


def home(request):
    context = dict()
    email = request.session.get('email')
    if email:
        context['msg'] = "Already logged in!"
        return redirect('/assessment')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.filter(email=email)
            if user:
                login(request, user[0])
                request.session['email'] = email
                context['msg'] = "User " + email + " logged in."
                return redirect('/assessment')
            else:
                context['msg'] = "Wrong email or password"
    return render(request, 'index.html', context)


def assessment(request):
    return render(request, 'assessment.html', {'quiz': Quiz.objects.all()})


def signout(request):
    context = {}
    email = request.session.get('email')
    if email == '':
        context['msg'] = "No one has logged in!"
    else:
        context['msg'] = "User " + email + " logged out. Login again!"
        logout(request)
        request.session['email'] = ''
    return redirect('/')
