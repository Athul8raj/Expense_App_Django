import django_filters
from .models import Expenses

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Expenses
        fields = ['exp_name','date_uploaded','total_price',]

