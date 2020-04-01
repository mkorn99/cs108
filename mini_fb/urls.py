#file: profiles/urls.py
#description: direct URL requests to view functions

from django.urls import path
from .views import ShowAllProfileView, ShowProfilePageView

urlpatterns = [
    path('', ShowAllProfileView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'), 
]