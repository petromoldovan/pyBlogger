from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        # styled all fields. Cannot do otherwise as UserCreationForm is django form.
        classes = 'form-control'
        self.fields['username'].widget.attrs['class'] = classes
        self.fields['email'].widget.attrs['class'] = classes
        self.fields['first_name'].widget.attrs['class'] = classes
        self.fields['last_name'].widget.attrs['class'] = classes
        self.fields['password1'].widget.attrs['class'] = classes
        self.fields['password2'].widget.attrs['class'] = classes
