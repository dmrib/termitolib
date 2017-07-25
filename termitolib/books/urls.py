from django.conf.urls import url

from .views import BookCreateView


urlpatterns = [
                url(r'^register/$', BookCreateView.as_view(), name='create'),
]
