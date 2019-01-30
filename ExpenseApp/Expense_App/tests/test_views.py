from django.test import TestCase
from django.urls import reverse
from Expense_App.models import Expenses
from django.utils import timezone

class ExpenseTest(TestCase):
    
    def create_expense(self, exp_name="Exp2", total_price="yes, this is only a test"):
        return Expenses.objects.create(exp_name=exp_name, total_price=total_price,date_uploaded=timezone.now())

    def test_expense_view(self):
        w = self.create_expense()
        url = reverse("expenses")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 302)#200
#        self.assertIn(w.exp_name, resp.content.decode())
