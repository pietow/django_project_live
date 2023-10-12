from django import template

register = template.Library()

@register.simple_tag
def hello_world(value='Bla'):
    return f'Hello world {value}'