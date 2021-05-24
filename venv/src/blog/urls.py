from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView
)

app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    path('uptade/<int:id>', ArticleUpdateView.as_view(), name='article-uptade')
]