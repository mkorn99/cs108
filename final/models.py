#file: final/models.py
#author:Matthew Korn
#description: Stores the 3 models created within the database of Profile, Workout and Image
#Each model has the aspects that encapsulate the model'''

# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the idea of a profile and necessary information needed for submission'''

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    height = models.TextField(blank=True)
    weight = models.TextField(blank=True)
   
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    #friends = models.ManyToManyField("self")
    

    def __str__ (self):
        '''Return a string representation of this profile'''
        return '"%s" - %s - %s' % (self.first_name, self.last_name, self.image_url)

    def get_workout(self):
        '''Returns a Workout that was entered for this person. Filters by profile'''

        #get workout associated with the user
        s = Workout.objects.filter(profile=self.pk)
        return s

    def get_absolute_url(self):
        '''Return a URL to display this workout object, reverts back to profile page'''
        #return to profile page
        return reverse ("show_profile_page", kwargs={"pk":self.pk})

    def get_all_images(self):
        '''Returns queryset of all images for this person.'''

        #gets the image associated with the profile
        images = Image.objects.filter(profile=self.pk)
        return images

    

    def get_workout_feed(self):
        '''Creates a workout feed for all users to view in the all user feed'''

        #show object by profile
        news = Workout.objects.filter(profile=self.pk)
        return news


    

    

class Workout(models.Model):
    '''Model the data attributes of the workouts to be entered and user to view'''

    timestamp = models.TimeField(auto_now_add=True)
    workout = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    duration = models.TextField(blank=True)
    

    def __str__ (self):
        '''Return a string representation of this workout'''
        return '"%s" - %s - %s' % (self.timestamp, self.workout, self.duration )


class Image(models.Model):
    '''Represents an image, which is associated with a workout if desired'''

    #image file field
    image_file = models.ImageField(blank=True)

    #associated image with a profile
    profile = models.ForeignKey('Profile', on_delete= models.CASCADE)
    
    #image url field
    image_url = models.URLField(blank=True)

    def __str__ (self):
        '''Return a string representation of this workout image'''
        
        #if else logic to include image url or image file
        if self.image_url:

            return self.image_url

        else:
            return self.image_file.url
 


    
