from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Expenses
from .forms import DocumentForm
from django.contrib import messages
from .filter import UserFilter

def index(request):
    return render(request,'index.html')

@login_required
def expenses(request):
    expenses = Expenses.objects.all()

    return render(request, 'expenses.html', {'expenses':expenses})


@login_required
def add(request):
    if request.method == 'POST' and request.FILES['image']:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    else:
        form = DocumentForm()
    return render(request, 'add_expenses.html', {'form': form})


@login_required
def delete_expenses(request,id_value):
    expenses = Expenses.objects.filter(id=id_value) 
    if expenses:
        expenses.delete()
        return redirect('expenses')
    else:
        messages.info(request,f'You are not allowed to do this action!')
        return redirect('expenses')
        
@login_required
def filter_expenses(request):
    unique_field = Expenses.objects.all()
    user_filter = UserFilter(request.GET, queryset=unique_field)
    return render(request, 'filter.html', {'filter': user_filter})

@login_required
def view_expenses(request,value):
    expense = Expenses.objects.filter(id=value)
    if expense:
        return render(request,'view_expense.html',{'expense': expense})    
            