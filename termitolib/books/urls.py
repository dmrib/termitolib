from django.conf.urls import url
from django.views.generic import TemplateView

from .views import BookCreateView, BookSearchListView, BookDetailView, BookDeleteView, BookUpdateView


urlpatterns = [
                url(r'^register/$', BookCreateView.as_view(), name='register'),
                url(r'^search$', TemplateView.as_view(template_name='books/book_search.html'), name='search'),
                url(r'^search_result/$', BookSearchListView.as_view(), name='search-result'),
                url(r'^(?P<pk>[-\w]+)/$', BookDetailView.as_view(), name='book-detail'),
                url(r'^(?P<pk>[\w-]+)/delete$', BookDeleteView.as_view(), name='book-delete'),
                url(r'^(?P<pk>[\w-]+)/update$', BookUpdateView.as_view(), name='book-update'),
]
