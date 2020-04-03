from django import forms
from .models import Profile, StatusMessage


class CreateProfileForm(forms.ModelForm):
    '''Create a profile class'''
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email", required=True)
    image_url = forms.CharField(label="image_url", required=True)


    

    class Meta:
        '''Associate this form with the quote model'''
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email_address', 'image_url',]

class UpdateProfileForm(forms.ModelForm):
    '''Create a update profile class'''
    
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email", required=True)
    image_url = forms.CharField(label="image_url", required=True)


    

    class Meta:
        '''Associate this form with the profile model'''
        model = Profile
        fields = ['city', 'email_address', 'image_url',]

class CreateStatusMessageForm(forms.ModelForm):
    '''Creates status message for a profile'''

    class Meta:
        '''Associates the form with the status message model'''
        model = StatusMessage
        fields = ['message']


    
    
    