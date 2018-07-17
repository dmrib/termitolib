from django import forms
from .models import Loan

from books.models import Book

class LoanForm(forms.ModelForm):
    code = forms.CharField(label='Book Code')

    class Meta:
        model = Loan
        fields = [
                    'to',
        ]
