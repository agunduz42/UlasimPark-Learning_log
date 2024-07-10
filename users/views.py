from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('learning_logs:index')
            ...
        else:
            messages.error(request, ("Username or password is wrong!"))
            return redirect('login') # should be a path name inside urls be careful
    else:
        return render(request, 'users/login_view.html', {})

def logout_view(request):
    logout(request)
    # you succesfully logged out message can be added
    return redirect('learning_logs:index')

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        # process completed form
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # log the user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse(('learning_logs:index')))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)