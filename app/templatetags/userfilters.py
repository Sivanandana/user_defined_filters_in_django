from django import template
register=template.Library()
def swap(data):
    return data.swapcase()
register.filter('swap',swap)

@register.filter()
def remove(data,arg):
    return data.replace(arg,'RS')
#register.filter('remove',remove)
@register.filter()
def count(data,arg):
    return data.count(arg)

@ register.filter()
def count(data,arg):
    c=0
    for i in range(len(data)):
        if data[i:i+len(arg)]==arg:
            c+=1
    return c
@ register.filter()
def upper(data):
    return data.upper()
@ register.filter()
def upper(krish):
    return krish.upper()
@ register.filter()
def lower(data):
    return data.lower()