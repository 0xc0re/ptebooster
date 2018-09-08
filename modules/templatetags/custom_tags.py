from django import template

register = template.Library()


@register.filter
def strip(value):
    print((value.strip(',.:; ')).lower())
    return (value.strip(',.:; ')).lower()