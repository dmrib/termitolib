from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import BookForm
from .models import Book

class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = 'books/book_register.html'
    form_class = BookForm
    success_url = '/'
    login_url = '/login'

    def form_valid(self, form):
        book = form.save(commit=False)
        book.registered_by = self.request.user
        return super(BookCreateView, self).form_valid(form)
