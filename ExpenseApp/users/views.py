from django.shortcuts import render,redirect
from .forms import UserCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method=='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
            
         
    else:
        form = UserCreateForm()
    return render(request,'users/user_register.html',{'form':form}) 

@login_required    
def profile(request):
    return render(request,'users/profile.html')
    