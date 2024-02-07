from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in'))
            return redirect('home')
        else:
            messages.success(request, ('Error logging in - please try again'))
            return redirect('home')
        
    return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate & login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have been registered! Welcome to Django CRM'))
            return redirect('home')
            
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    
    return render(request, 'signup.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # get the record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, ('You must be logged in.'))
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, ('You Just Deleted a Record'))
        return redirect('home')
    else:
        messages.success(request, ('You must be logged in.'))
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    
    if request.user.is_authenticated:
        if request.method == 'POST' and form.is_valid():
            add_record = form.save()
            messages.success(request, ('You Just Added a Record'))
            return redirect('home')
    else:
        messages.success(request, ('You must be logged in.'))
        return redirect('home')
    
    return render(request, 'add_record.html', {'form':form})