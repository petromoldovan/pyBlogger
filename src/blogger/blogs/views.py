from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created']
    #ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        likes_obj = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes_obj.get_total_likes()
        context["total_likes"] = total_likes
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post-new.html'
    #give all fields in form
    #fields = '__all__'
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post-update.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'post-delete.html'
    #where to navigate on success
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories-list.html', {'cat_menu_list': cat_menu_list})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id_btn_value'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))