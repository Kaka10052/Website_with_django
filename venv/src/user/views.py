from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404

from .decorators import unauthorized_user, allowed_groups
from .forms import CreateUserForm
from .models import Reader

from books.models import Book


@unauthorized_user
def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='reader')
            user.groups.add(group)
            Reader.objects.create(
                user=user,
                username=user.username
            )
            messages.success(request, 'Account was created.')
            return redirect('login-view')

    context = {
        'form': form
    }
    return render(request, 'user/user_register.html', context)


@unauthorized_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong username OR password')
    context = {}
    return render(request, 'user/user_login.html', context)


@login_required(login_url='login-view')
def logoutUser(request):
    logout(request)
    return redirect('login-view')


@login_required(login_url='login-view')
@allowed_groups(['reader', 'admin', 'moderator'])
def own_profile_view(request):
    context = {}
    return render(request, 'user/user_profile.html', context)


@login_required(login_url='login-view')
@allowed_groups(['reader', 'admin', 'moderator'])
def own_bookcase_view(request):
    books = request.user.reader.books.all()
    print(books)
    context = {
        'books': books
    }
    return render(request, 'user/user_bookcase.html', context)

def other_user_view(request, id):
    user_profile = get_object_or_404(Reader, id=id)
    print(user_profile)
    context = {
        'user':user_profile,
        'books': user_profile.books.all()
    }
    return render(request, 'user/user_bookcase.html', context)


