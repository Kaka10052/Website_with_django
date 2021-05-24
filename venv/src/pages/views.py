from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def items_view(request, *args, **kwargs):
    my_dict = {
        'name' : 'item',
        'number' : 123,
        'items' : ['case', 'knife', 'weapon']
    }
    return render(request, 'items.html', my_dict)

