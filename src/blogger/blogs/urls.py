from django.urls import path
from .views import PostListView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post-details/<int:pk>', PostDetailView.as_view(), name='post-details'),
    path('post-new/', AddPostView.as_view(), name='post-new'),
    path('categories/new', AddCategoryView.as_view(), name='categories-new'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),

    path('category/<str:cats>/', CategoryView, name='categoryview'),
    path('categories/', CategoryListView, name='categorylist'),

    path('like/<int:pk>', LikeView, name='like-post'),

    path('article/<int:pk>/comment', AddCommentView.as_view(), name='comment-new'),
]
