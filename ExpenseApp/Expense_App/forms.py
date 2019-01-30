from django import forms
from .models import Expenses

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('exp_name','total_price', 'image')