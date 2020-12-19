from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})



class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DeleteView):
    model = Post
    template_name = 'article.details.html'
