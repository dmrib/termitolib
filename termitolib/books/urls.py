from django.conf.urls import url
from django.views.generic import TemplateView

from .views import BookCreateView


urlpatterns = [
                url(r'^register/$', BookCreateView.as_view(), name='register'),
                url(r'^search$', TemplateView.as_view(template_name='books/book_search.html'), name='search')
]
