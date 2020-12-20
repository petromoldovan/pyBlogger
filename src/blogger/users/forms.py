from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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

class EditProfileForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        # styled all fields. Cannot do otherwise as UserCreationForm is django form.
        classes = 'form-control'
        self.fields['username'].widget.attrs['class'] = classes
        self.fields['email'].widget.attrs['class'] = classes
        self.fields['first_name'].widget.attrs['class'] = classes
        self.fields['last_name'].widget.attrs['class'] = classes
        self.fields['password'].widget.attrs['class'] = classes

class PasswordChangeFormOwn(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')