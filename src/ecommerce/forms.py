from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):

    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control",
                   'id': "form_full_name",
                   'placeholder': "Your Full Name"
                   }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Your Email ID'
                   }
        )
    )
    contact = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'Your Information'
                   }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "gmail.com" in email:
            return email
        raise forms.ValidationError("Email has to be gmail.com")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        usernamefilter = User.objects.filter(username=username)
        if usernamefilter:
            raise forms.ValidationError("Username already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        emailfilter = User.objects.filter(email=email)
        if emailfilter:
            raise forms.ValidationError("email already taken")
        return email

    def clean(self):
        password = self.cleaned_data.get("Password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Password must match")
        return self.cleaned_data
