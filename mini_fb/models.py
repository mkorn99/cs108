
from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the idea of a profile (i.e., text)'''

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__ (self):
        '''Return a string representation of this object'''
        return '"%s" - %s - %s - %s' % (self.first_name, self.last_name, self.city, self.email_address)

    def get_status_message(self):
        '''Returns a status message for this person.'''

        message = StatusMessage.objects.filter(profile=self.pk)
        return message


class StatusMessage(models.Model):
    '''Model the data attributes of status messages'''

    timestamp = models.TimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__ (self):
        '''Return a string representation of this object'''
        return '"%s" - %s' % (self.timestamp, self.message)
