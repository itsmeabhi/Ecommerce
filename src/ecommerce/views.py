from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'content': 'Home Page'
    }
    return render(request, "homepage.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'content': 'Contact Page',
        'form': contact_form,
    }
    if contact_form.is_valid():
        return redirect("/")
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
        print login_form.cleaned_data
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print "Error"

    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        'form': register_form
    }
    if register_form.is_valid():
        print register_form.cleaned_data
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username, email, password)

    return render(request, "auth/register.html", context)



