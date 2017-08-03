from django.conf.urls import url
from django.views.generic import TemplateView
from .views import RegisterView

urlpatterns = [
    url(r'^signup/$', RegisterView.as_view(), name='signup'),
]
