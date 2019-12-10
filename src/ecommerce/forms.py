from django import forms


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
                   'placeholder': 'your Email ID'
                   }
        )
    )
    contact = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'your Information'
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
    password = forms.CharField()
    confirmpassword = forms.CharField()
