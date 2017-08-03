from django import forms
from .models import Loan

from books.models import Book

class LoanForm(forms.ModelForm):
    code = forms.CharField(label='Book Code')

    def clean_code(self):
         if not Book.objects.filter(code = self.cleaned_data.get('code')).exists():
            raise forms.ValidationError("Not a valid book code")

    class Meta:
        model = Loan
        fields = [
                    'to',
        ]
