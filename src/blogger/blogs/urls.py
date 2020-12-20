from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('categories/new', AddCategoryView.as_view(), name='categories-new'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),

    path('category/<str:cats>/', CategoryView, name='categoryview'),
    path('categories/', CategoryListView, name='categorylist'),

    path('like/<int:pk>', LikeView, name='like-post'),
]
