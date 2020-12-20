from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DeleteView):
    model = Post
    template_name = 'article.details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #give all fields in form
    #fields = '__all__'
    #fields = ('title', 'body')