from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

    def render_to_response(self, context, **kwargs):
        print(self.request.COOKIES.get('my_cookie'))
        if self.request.COOKIES.get('my_cookie') == 'my_cookie_value':
            response = HttpResponse('With cookie')
            return response
        return super().render_to_response(context, **kwargs)

class AboutPageView(TemplateView):
    template_name = "about.html"


def homePageView(request):
    # print(request)
    # print(request.method == 'GET')
    # print(request.COOKIES)
    context = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'Hello',
        'first': [1, 2, 3],
        'second': [4, 5, 6],
        'today': datetime.now(),
        'notes': "<strong>Note:</strong> Always learn something new!",
        'js_inject':"<script>alert('Hello World')</script>"
    }
    response_render = render(request, 'home2.html', context)
    print('Response:', response_render)
    print('####################################################')
    response = HttpResponse('<h1>Hello</h1>')
    response.write('<div>Hello2</div>')
    response.write('<div>Hello2</div>')
    response.set_cookie('my_cookie', 'my_cookie_value')
    print(response)
    print('####################################################')
    print(HttpResponseForbidden('you are not allowed to enter'))
    print(HttpResponseServerError())
    return response_render

