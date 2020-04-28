#file: final/urls.py
#Author:matthew korn
#description: direct URL requests to view functions, urls with 'pk' are within a larger url

from django.urls import path
from .views import *
from .forms import *

urlpatterns = [
    path('show_all_profiles', ShowAllProfileView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), 
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/<int:pk>/post_workout', create_workout, name='post_workout'),
    path('profile/create_workout', CreateWorkoutView.as_view(), name='create_workout'),
    path('profile/<int:profile_pk>/delete_workout/<int:workout_pk>',DeleteWorkoutView.as_view(), name='delete_workout'),
    path('profile/post_workout2', create_workout2, name='post_workout2'),
    path('', HomePageView.as_view(), name='home'),
    path('random', RandomWorkoutPageView.as_view(), name="random_workout"),
    path('show_workout_feed',ShowWorkoutFeedView.as_view(), name='show_workout_feed'),

]
    
    
