from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import ProcessFormView
from django.urls import reverse

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


class BookSearchListView(ListView):
    template_name = 'books/book_search_result.html'
    context_object_name = 'books'

    def get_queryset(self):
        term = self.request.GET.get('term')
        result = Book.objects.filter(Q(name__icontains=term) |
                                     Q(authors__icontains=term) |
                                     Q(tags__icontains=term) |
                                     Q(publisher__icontains=term) |
                                     Q(isbn__icontains=term) |
                                     Q(shelf__icontains=term) |
                                     Q(code__icontains=term)
                 )
        return result


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/'
    context_object_name = 'book'


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_update_form.html'
    fields = ['name', 'authors', 'tags', 'publisher', 'isbn', 'shelf', 'code',
              'copies']

    def get_success_url(self):
        return '/books/' + self.kwargs.get('pk')
