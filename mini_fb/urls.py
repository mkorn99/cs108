#file: profiles/urls.py
#description: direct URL requests to view functions

from django.urls import path
from .views import ShowAllProfileView

urlpatterns = [
    path('', ShowAllProfileView.as_view(), name='profile'),
    
]