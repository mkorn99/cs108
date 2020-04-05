# quotes/forms.py

from django import forms
from .models import Quote, Image

class CreateQuoteForm(forms.ModelForm):
    '''A form to add new queries to the database.'''

    class Meta:
        '''Associate this form with the quote model'''
        model = Quote
        fields = ['person', 'text',]

class UpdateQuoteForm(forms.ModelForm):
    '''A form to update the quote to the database'''
    
    class Meta:
        '''Associate this form with the quote model'''
        model = Quote
        fields = ['person', 'text',]

class AddImageForm(forms.ModelForm):
    '''A form to collect an image from the user'''

    class Meta:
        model = Image
        fields = ["image_file",]
