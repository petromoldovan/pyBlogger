from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('password/', PasswordsChangeView.as_view(), name='change-password'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password_success/', views.password_success, name='password_success'),
]
