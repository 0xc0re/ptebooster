from django import template
from random import shuffle
register = template.Library()


@register.filter
def strip(value):
    print((value.strip(',.:; ')).lower())
    return (value.strip(',.:; ')).lower()

@register.filter
def shuffle_list(answer):
    shuffle(answer)
    return answer 