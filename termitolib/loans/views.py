from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.urls import reverse

from .forms import LoanForm
from .models import Loan
from books.models import Book

User = settings.AUTH_USER_MODEL


class LoanCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'loans/loan_register.html'
    form_class = LoanForm
    success_url = '/'
    login_url = '/login'
    permission_required = 'is_staff'


    def form_valid(self, form):
        loan = form.save(commit=False)
        loan.by = self.request.user
        loan.item = Book.objects.get(code=form.cleaned_data['code'])
        return super(LoanCreateView, self).form_valid(form)


class LoansListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'loans/loans_return.html'
    context_object_name = 'loans'
    login_url = '/login'
    permission_required = 'is_staff'

    def get_queryset(self):
        result = Loan.objects.all()
        return result


class MyLoansListView(LoginRequiredMixin, ListView):
    template_name = 'loans/loans_myloans.html'
    context_object_name = 'loans'
    login_url = '/login'

    def get_queryset(self):
        user = self.request.user
        result = Loan.objects.filter(to = user.id)
        return result


class LoanDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Loan
    success_url = '/'
    context_object_name = 'loan'
    login_url = '/login'
    permission_required = 'is_staff'


class LoanNotifyView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Loan
    success_url = '/'
    context_object_name = 'loan'
    login_url = '/login'
    permission_required = 'is_staff'
    template_name = 'loans/loans_notify.html'

    def get_context_data(self, **kwargs):
        context = super(LoanNotifyView, self).get_context_data(**kwargs)
        mail = self.compose(context['loan'])
        send_mail('Delayed loan at termitolib', mail['message'], 'termitolib@gmail.com', [mail['to']])
        return context

    def compose(self, loan):
        mail = {}
        mail['message'] = f'\n\nThis is a reminder that you got a delayed loan at termitolib! Plase return {loan.item.name}.'
        mail['to'] = loan.to.email
        return mail
