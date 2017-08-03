from django.conf.urls import url

from .views import LoanCreateView, LoansListView, LoanDeleteView, LoanNotifyView, MyLoansListView

urlpatterns = [
                url(r'^register/$', LoanCreateView.as_view(), name='register'),
                url(r'^return/$', LoansListView.as_view(), name='return'),
                url(r'^myloans/$', MyLoansListView.as_view(), name='myloans'),
                url(r'^(?P<pk>[-\w]+)/notify$', LoanNotifyView.as_view(), name='notify'),
                url(r'^(?P<pk>[\w-]+)/delete$', LoanDeleteView.as_view(), name='delete'),
]
