from django import forms
from .models import Post, Category

# prepare cats choices
cats = Category.objects.all().values_list('name', 'name')
catsChoices = []
for item in cats:
    catsChoices.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tab_name', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tab_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Placeholder text'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'userid', 'type': 'hidden'}),
            'category': forms.Select(choices=catsChoices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }