from django.test import TestCase
from Expense_App.models import Expenses
from django.utils import timezone

class ExpenseTest(TestCase):

    def create_expense(self, exp_name="Exp1", total_price="yes, this is only a test"):
        return Expenses.objects.create(exp_name=exp_name, total_price=total_price,date_uploaded=timezone.now())

    def test_expense_creation(self):
        w = self.create_expense()
        self.assertTrue(isinstance(w, Expenses))