#File Name: final/forms.py
#Author:Matthew Korn
#Description:'''Encapsulates the forms for Create Profile, Update Profile and Create Workout and the necessary fields for each form'''


from django import forms
from .models import Profile, Workout


class CreateProfileForm(forms.ModelForm):
    '''Create a profile class and each paramter necessary to create a profile'''
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    height = forms.CharField(label="Height", required=True)
    weight = forms.CharField(label="Weight (in lbs)", required=True)
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email", required=True)
    image_url = forms.CharField(label="image_url", required=True)
    

    class Meta:
        '''Associate this form with the profile model and displays the necessary fields'''
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email_address', 'image_url','height', 'weight']

class UpdateProfileForm(forms.ModelForm):
    '''Create a update profile class to edit information of the profile'''
    
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email", required=True)
    image_url = forms.CharField(label="image_url", required=True)
    height = forms.CharField(label="Height", required=True)
    weight = forms.CharField(label="Weight (in lbs)", required=True)


    class Meta:
        '''Associate this form with the profile model and show the editable fields'''
        model = Profile
        fields = ['city', 'email_address', 'image_url', 'height', 'weight',]

class CreateWorkoutForm(forms.ModelForm):
    '''Creates workout for a profile with workout and duration'''

    image = forms.ImageField(label="image", required=False)
    class Meta:
        '''Associates the form with the Workout model and creates the necessary fields'''
        model = Workout
        fields = ['profile', 'workout','duration','image']


    
    
    