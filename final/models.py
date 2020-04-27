

# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the idea of a profile (i.e., text)'''

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
        return '"%s" - %s - %s - %s' % (self.first_name, self.last_name, self.city, self.email_address)

    def get_workout(self):
        '''Returns a Workout that was entered for this person. Filters by profie'''

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
        '''Creates a workout feed for all users'''

        #show object by profile
        news = Workout.objects.filter(profile=self.pk)
        return news


    

    

class Workout(models.Model):
    '''Model the data attributes of the workouts to be entered'''

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

    
    image_file = models.ImageField(blank=True)
    profile = models.ForeignKey('Profile', on_delete= models.CASCADE)
    image_url = models.URLField(blank=True)

    def __str__ (self):
        '''Return a string representation of this workout image'''
        if self.image_url:

            return self.image_url

        else:
            return self.image_file.url
 


    
