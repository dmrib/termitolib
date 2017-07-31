from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .forms import LoanForm
from .models import Loan
from books.models import Book

class LoanCreateView(LoginRequiredMixin, CreateView):
    template_name = 'loans/loan_register.html'
    form_class = LoanForm
    success_url = '/'
    login_url = '/login'

    def form_valid(self, form):
        loan = form.save(commit=False)
        loan.by = self.request.user
        loan.item = Book.objects.get(code=form.cleaned_data['code'])
        return super(LoanCreateView, self).form_valid(form)
