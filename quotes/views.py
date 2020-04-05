from django.shortcuts import render

# Create your views here.
from .models import Quote, Person, Image
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateQuoteForm, UpdateQuoteForm
import random
from django.urls import reverse
from django.shortcuts import redirect

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

class PersonPageView(DetailView):
    '''Show all quotes and all images for one person'''

    model = Person
    template_name = 'quotes/person.html'
    #context_object_name = 'person'

    def get_context_data(self, **kwargs):
        '''Retuns a dictionary with context data for this template to use.'''

        context = super(PersonPageView, self).get_context_data(**kwargs)
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form
        return context

class CreateQuoteView(CreateView):
    '''A view to create a new quote and save it to the database'''

    form_class = CreateQuoteForm
    template_name = "quotes/create_quote.html"

class UpdateQuoteView(UpdateView):
    '''A view to create a new quote and save it to the database'''

    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote.html"
    queryset = Quote.objects.all()


class DeleteQuoteView(DeleteView):
    '''A view to delete a new quote and remove it to the database'''

    
    template_name = "quotes/delete_quote.html"
    queryset = Quote.objects.all()
    success_url = "../../all"

    def get_success_url(self):
        '''Return the URL to which we should be directed after the delete'''

        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first()
        person = quote.person
        return reverse('person', kwargs={'pk':person.pk})


def add_image(request, pk):
    '''A custom view functiokn to handle the submission of an image upload'''
    person = Person.objects.get(pk=pk)
    form = AddImageForm(request.Post or None, request.FILES or None)
    if form.is_valid():
        image = form.save(commit=False)
        image.person = person
        image.save()

    else: 
        print("Error: the form is not valid")

    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)