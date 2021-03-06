
from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the idea of a profile (i.e., text)'''

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def __str__ (self):
        '''Return a string representation of this object'''
        return '"%s" - %s - %s - %s' % (self.first_name, self.last_name, self.city, self.email_address)

    def get_status_message(self):
        '''Returns a status message for this person.'''

        message = StatusMessage.objects.filter(profile=self.pk)
        return message

    def get_absolute_url(self):
        '''Return a URL to display this quote object'''
        return reverse ("'show_profile_page', 'update_profile'", kwargs={"pk":self.pk})

    def get_all_images(self):
        '''Return sa queryset of all images for this person.'''

        images = Image.objects.filter(profile=self.pk)
        return images

    def get_friends(self):
        '''Returns a friends list for this person.'''

        friends = Profile.objects.filter(friends=self.pk)
        return friends

    def get_news_feed(self):
        '''Creates a news feed by profile'''

        friends = self.get_friends()
        news = StatusMessage.objects.filter(profile__in= self.get_friends())
        return news

    def get_friend_suggestions(self):
        '''Obtain and return set of possible friends'''

        possible_friends = Profile.objects.exclude(pk__in=self.get_friends()).exclude(id=self.pk)
        return possible_friends
    


class StatusMessage(models.Model):
    '''Model the data attributes of status messages'''

    timestamp = models.TimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__ (self):
        '''Return a string representation of this object'''
        return '"%s" - %s' % (self.timestamp, self.message)


class Image(models.Model):
    '''Represents an image, which is associated with a person'''

    
    image_file = models.ImageField(blank=True)
    profile = models.ForeignKey('Profile', on_delete= models.CASCADE)
    image_url = models.URLField(blank=True)

    def __str__ (self):
        '''Return a string representation of this object'''
        if self.image_url:

            return self.image_url

        else:
            return self.image_file.url
 


    
