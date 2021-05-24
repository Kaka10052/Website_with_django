from django.shortcuts import redirect
from django.http import HttpResponse

def unauthorized_user(view_function):
    def decorator(request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return redirect('home')
        return view_function(request, *args, **kwargs)
    return decorator

def allowed_groups(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_func(request, *args, **kwargs):
            user_group = None
            if request.user.groups.exists():
                # We assume that user has only 1 role
                user_group = request.user.groups.all()[0].name
            if user_group in allowed_roles:
                return view_function(request, *args, **kwargs)
            return HttpResponse('You are not allowed to be here! Go away!')
        return wrapper_func
    return decorator

