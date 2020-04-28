#file:final/admin.py
#author:Matthew Korn
#description: '''Register the models in the database'''

from django.contrib import admin




# Register your models here.
from .models import Profile, Workout, Image
admin.site.register(Profile)
admin.site.register(Workout)
admin.site.register(Image)
