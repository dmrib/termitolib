from django.conf.urls import url

from .views import LoanCreateView

urlpatterns = [
                url(r'^register/$', LoanCreateView.as_view(), name='register'),
]
