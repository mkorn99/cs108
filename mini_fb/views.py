from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
# Create your views here.
from .models import Profile, StatusMessage
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm

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

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

    # obtain the default context data (a dictionary) from the superclass; 
    # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
    # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
    # return this context dictionary
        return context

def create_status_message(request, pk):
    
    '''Process a form submission to post a new status message.'''
     
    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)

     # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

         # read the data from this form submission
        message = request.POST['message']

            # save the new status message object to the database
        if message:

            sm = StatusMessage()
            sm.profile = profile
            sm.message = message
            sm.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))

class CreateProfileView(CreateView):
    '''Creates a new profile'''

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

class UpdateProfileView(UpdateView):
    '''Updates an existing profile'''

    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'
    queryset = Profile.objects.all()

    
    
