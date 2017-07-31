from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    code = forms.CharField(label='Book Code')

    class Meta:
        model = Loan
        fields = [
                    'to',
        ]
