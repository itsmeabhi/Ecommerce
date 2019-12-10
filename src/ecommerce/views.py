from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm


def home_page(request):
    context = {
        'content': 'Home Page'
    }
    return render(request, "homepage.html", context)


def contact_page(request):
    import ipdb
    ipdb.set_trace()
    contact_form = ContactForm(request.POST or None)
    context = {
        'content': 'Contact Page',
        'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


def about_page(request):
    context = {
        'content': 'About Page'
    }
    return render(request, "homepage.html", context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        'form': login_form
    }
    print request.user.is_authenticated()
    if login_form.is_valid():
        impo
        print login_form.cleaned_data
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/login")
        else:
            print "Error"

    return render(request, "auth/login.html", context)




