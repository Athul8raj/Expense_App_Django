from django.test import TestCase
from Expense_App.models import Expenses
from django.utils import timezone
from Expense_App.forms import DocumentForm

class ExpenseTest(TestCase):
    
    def create_expense(self, exp_name="Exp2", total_price="yes, this is only a test"):
        return Expenses.objects.create(exp_name=exp_name, total_price=total_price,date_uploaded=timezone.now())
    
    def test_valid_form(self):
        w = Expenses.objects.create(exp_name="Exp2", total_price="yes, this is only a test")
        data = {'exp_name': w.exp_name, 'total_price': w.total_price,}
        form = DocumentForm(data=data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_form(self):
        w = Expenses.objects.create(exp_name="Exp2", total_price="")
        data = {'exp_name': w.exp_name, 'total_price': w.total_price,}
        form = DocumentForm(data=data)
        self.assertFalse(form.is_valid())
