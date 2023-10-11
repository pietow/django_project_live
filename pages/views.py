from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"


def homePageView(request):
    context = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'Hello',
        'first': [1, 2, 3],
        'second': [4, 5, 6],
        'today': datetime.now() 
    }
    response = render(request, 'home2.html', context)
    print('Response:', response)
    return response

