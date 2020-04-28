#file name: final/views.py
#author:Matthew Korn 
#description:'''Includes the views of the webserver such as Show all profiles, Profile Page, Create profile, Update Profile,
# Create Workout, Delete Workout, Homepage, Random Workout(Work out of the day), Show Workout Feed (All User feed)'''

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
import random

# Create your views here.
# Create your views here.
from .models import Profile, Workout, Image
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import CreateProfileForm, UpdateProfileForm, CreateWorkoutForm

class ShowAllProfileView(ListView):
    '''Create a subclass of ListView to display all profiles in database'''

    model = Profile
    template_name = 'final/show_all_profiles.html'
    context_object_name = 'all_profiles_list'


class ShowProfilePageView(DetailView):
    '''Obtains data for one profile record'''

    model = Profile
    template_name = 'final/show_profile_page.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

    # obtain the default context data (a dictionary) from the superclass; 
    # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
    # create a new CreatWorkoutForm, and add it into the context dictionary
        form = CreateWorkoutForm()
        context['create_workout_form'] = form
    # return this context dictionary
        return context

def create_workout(request, pk):
    
    '''Process a form submission to post a new workout.'''
     
    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)
    form = CreateWorkoutForm(request.POST or None, request.FILES or None)
     # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

         # read the data from this form submission
        workout = request.POST['workout']

            # save the new workout object to the database
        if workout:

            sm = form.save(commit=False)
            sm.profile = profile
            sm.workout = workout
            
            sm.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))

class CreateProfileView(CreateView):
    '''Creates a new profile for the database'''

    form_class = CreateProfileForm
    template_name = 'final/create_profile_form.html'

class UpdateProfileView(UpdateView):
    '''Updates an existing profile from the database'''

    form_class = UpdateProfileForm
    template_name = 'final/update_profile_form.html'
    queryset = Profile.objects.all()

class DeleteWorkoutView(DeleteView):
    '''A view to delete a new workout and remove it to the database'''

    
    template_name = "final/delete_workout.html"
    queryset = Workout.objects.all()
    

    def get_success_url(self):
        '''Return the URL to which we should be directed after the delete'''

        #return back to the profile page after the delete action
        profile_pk = self.kwargs['profile_pk']
        return reverse('show_profile_page', kwargs={'pk':profile_pk})

    def get_context_data(self, **kwargs):
        '''Returns a dictionary with context data for this template to use.'''

        #creates ability to delete workout on profile page
        context = super(DeleteWorkoutView, self).get_context_data(**kwargs)

        #gets workout object to delete
        work = Workout.objects.get(pk=self.kwargs['workout_pk'])

        #create dictionary
        context['work'] = work
        #return dictionary
        return context

    def get_object(self):
        '''Returns the workout associated with the profile'''
        
        #uses profile and workout primary key to return workout that is attached to a profile
        profile_pk = self.kwargs['profile_pk']
        workout_pk = self.kwargs['workout_pk']

        return Workout.objects.get(pk=workout_pk)
        



class CreateWorkoutView(CreateView):
    '''Creates a new workout and assigns to a user'''

    form_class = CreateWorkoutForm
    template_name = 'final/create_workout.html'

def create_workout2(request):
    
    '''Process a form submission to post a workout.'''
     
    # find the profile that matches the `pk` in the URL
    
    form = CreateWorkoutForm(request.POST or None, request.FILES or None)
     # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

         # read the data from this form submission
        workout = request.POST['workout']
        profile = request.POST['profile']
        prof = Profile.objects.get(pk = profile)
            # save the new status message object to the database
        if workout:

            sm = form.save(commit=False)
            sm.profile = prof
            sm.workout = workout
            #sm.image = image
            #sm.duration = duration
            sm.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': profile}))


class HomePageView(TemplateView):
    '''A specialized version of TemplateView to display our home page'''

    template_name = "final/home.html"


class RandomWorkoutPageView(DetailView):
    '''Show one workout and duration selected at random'''

    model = Workout
    template_name = 'final/random_workout.html'
    context_object_name = 'random_workout'

    def get_object(self):
        '''Returns a single instance of a Workout Object, selected at random'''

        all_workout = Workout.objects.all()
        #selects a random workout in the database
        r = random.randint(0, len(all_workout) -1)
        q = all_workout[r]
        return q

class ShowWorkoutFeedView(ListView):
    '''Shows all workouts in the database'''

    model = Workout
    template_name = "final/show_workout_feed.html"
    context_object_name= "all_workouts"
    

    







