from django.urls import path
from .views import (detail_create_view,
                    dynamic_lookup_view,
                    addBook,
                    detail_delete_view,
                    detail_list_view,
                    detail_search_view,
                    categories_list_view,
                    search_list_view)

urlpatterns = [
    path('', detail_list_view, name='book-list'),
    path('create', detail_create_view, name='book-create'),
    path('categories', categories_list_view, name='categories-list'),
    path('categories/<str:category>', search_list_view, name='search-list'),
    path('search', detail_search_view, name='book-search'),
    path('add_book/<str:pk>', addBook, name='add_book_to_user'),
    path('<int:id>', dynamic_lookup_view, name='book-detail'),
    path('<int:id>/delete', detail_delete_view, name='book-delete')
    ]