from django.shortcuts import render

# Create your views here.
from .models import Quote
from django.views.generic import ListView, DetailView
import random

class HomePageView(ListView):
    '''Create a subclass of ListView to display all quotes'''

    model = Quote
    template_name = "quotes/home.html"
    context_object_name = "all_quotes_list"

class QuotePageView(DetailView):
    '''Show the details for one quote'''

    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    '''Show one quote selected at random'''

    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    def get_object(self):
        '''Returns a single instance of a Quote Object, selected at random'''

        all_quotes = Quote.objects.all()

        r = random.randint(0, len(all_quotes) -1)
        q = all_quotes[r]
        return q

         
