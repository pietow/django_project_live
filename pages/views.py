from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError

# Create your views here.
class ActiveRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('my_cookie') == 'my_cookie_value':
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden('You are not allowed to access')

def practice_view(request):
    context = {
            'list_of_numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'greeting': "Hello, World!",
            'user_info': {
                'first_name': "John",
                'last_name': "Doe",
                'email': "john.doe@example.com"
                },
            'is_vip': True,
            'notes': "<strong>Note:</strong> Always learn something new!"
            }
    return render(request, 'practice_page.html', context)

class HomePageView(TemplateView):
    template_name = "home.html"

    def render_to_response(self, context, **kwargs):
        print(self.request.COOKIES.get('my_cookie'))
        if self.request.COOKIES.get('my_cookie') == 'my_cookie_value':
            response = HttpResponse('With cookie')
            return response
        return super().render_to_response(context, **kwargs)

class AboutPageView(ActiveRequiredMixin ,TemplateView):
    template_name = "about.html"


def homePageView(request):
    # print(request)
    # print(request.method == 'GET')
    # print(request.COOKIES)
    print(request.headers)
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
    # print('Response:', response_render)
    # print('####################################################')
    response = HttpResponse('<h1>Hello</h1>')
    response.write('<div>Hello2</div>')
    response.write('<div>Hello2</div>')
    response.set_cookie('my_cookie', 'my_cookie_value')
    # print(response)
    # print('####################################################')
    # print(HttpResponseForbidden('you are not allowed to enter'))
    # print(HttpResponseServerError())
    return response_render

#### dipatch method from TemplateView:
    # def dispatch(self, request, *args, **kwargs):
    #     if request.method.lower() in self.http_method_names:
    #         handler = getattr(
    #             self, request.method.lower(), self.http_method_not_allowed
    #         )
    #     else:
    #         handler = self.http_method_not_allowed
    #     return handler(request, *args, **kwargs)


class ActiveRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('my_cookie') == 'my_cookie_value':
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden('You are not allowed to access')

class DashboardView(ActiveRequiredMixin, TemplateView):
    template_name = 'dashboard.html'