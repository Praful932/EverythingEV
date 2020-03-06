import random
from django import template

register = template.Library()

@register.simple_tag
def random_int():
    return random.randint(1,25)