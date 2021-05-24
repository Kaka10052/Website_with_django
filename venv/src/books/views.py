from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import BookForm, RawBookForm
from .filters import BookFilter

from user.decorators import allowed_groups

# Create your views here.
def detail_list_view(request):
    queryset = Book.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'book/book_list.html', context)

def categories_list_view(request):
    categories = Book.CATEGORY_CHOICES
    context = {
        'categories_list': categories
    }
    return render(request, 'book/categories_list.html', context)

def search_list_view(request, category=None):
    books = Book.objects.filter(category__exact=category)
    context = {
        'object_list': books
    }
    return render(request, 'book/book_list.html', context)


def detail_search_view(request):
    search_phrase = ''
    queryset = Book.objects.all()
    if request.method == 'POST':
        # request.POST is QueryDict
        search_phrase = request.POST['search']
        queryset = Book.objects.filter(title__contains = search_phrase)
    context = {
        'object_list': queryset,
    }
    return render(request, 'book/book_search.html', context)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Book, id=id)
    context = {
        'book': obj
    }
    return render(request, 'book/default.html', context)


@login_required(login_url='login-view')
@allowed_groups(['reader'])
def addBook(request, pk):
    book = Book.objects.get(id=pk)
    request.user.reader.books.add(book)
    print(book.title, 'was added to your account.')
    return redirect('home')


def detail_create_view(request):
    my_form = RawBookForm()
    if request.method == 'POST':
        # We can also send image for bookcover
        my_form = RawBookForm(request.POST, request.FILES)
        if my_form.is_valid():
            Book.objects.create(**my_form.cleaned_data)
            my_form = RawBookForm()
    context = {
        'form' : my_form
    }
    return render(request, 'book/book_create.html', context)


def detail_delete_view(request, id=id):
    obj = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {
        'object': obj
    }
    return render(request, 'book/book_delete.html', context)