from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('password/', PasswordsChangeView.as_view(), name='change-password'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password_success/', views.password_success, name='password_success'),

    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit_profile_page'),
]
