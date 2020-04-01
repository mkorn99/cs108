from django.shortcuts import render

# Create your views here.
# Create your views here.
from .models import Profile
from django.views.generic import ListView, DetailView

class ShowAllProfileView(ListView):
    '''Create a subclass of ListView to display all profiles'''

    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "all_profiles_list"


class ShowProfilePageView(DetailView):
    '''Obtains data for one profile record'''

    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'
