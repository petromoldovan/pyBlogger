from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post-list.html'
    ordering = ['-created']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        post_obj = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_obj.get_total_likes()
        context["total_likes"] = total_likes

        isLiked = False
        if post_obj.likes.filter(id=self.request.user.id).exists():
            isLiked = True

        context["isLiked"] = isLiked

        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post-new.html'

    # assign correct user to the profile
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post-update.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'post-delete.html'
    #where to navigate on success
    success_url = reverse_lazy('post-list')


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
    #isLiked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        #isLiked = True
    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment-new.html'
    #fields = '__all__'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)