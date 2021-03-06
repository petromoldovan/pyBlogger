from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm, EditProfileForm, PasswordChangeFormOwn, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from blogs.models import Profile

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('post-list')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeFormOwn
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, user_id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class EditProfilePageView(UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    #fields = ['bio', 'avatar', 'fb_url', 'website_url', 'linkedin_url', 'twitter_url']
    success_url = reverse_lazy('post-list')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'

    # assign correct user to the profile
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)