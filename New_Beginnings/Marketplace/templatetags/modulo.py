from django import template

register = template.Library()

@register.simple_tag
def modulo(num,val):
    return num / val