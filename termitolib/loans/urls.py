from django.conf.urls import url

from .views import LoanCreateView, LoansListView, LoanDeleteView

urlpatterns = [
                url(r'^register/$', LoanCreateView.as_view(), name='register'),
                url(r'^return/$', LoansListView.as_view(), name='return'),
                url(r'^(?P<pk>[\w-]+)/delete$', LoanDeleteView.as_view(), name='delete'),
]
