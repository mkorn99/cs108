from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
import time

def homePageView(request):
    '''Respons to an HTTP request with single web page'''

    response_html = '''
    <html>
    <h1>Hello, world!</h1>
    <p>
    This is our first Django web app
    <hr>
    This page was generate at %s.
    </html>
    ''' % time.ctime()

    return HttpResponse('Hello, world!')
