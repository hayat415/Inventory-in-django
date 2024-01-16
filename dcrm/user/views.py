from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='login')
def register(request):
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=CreateUserForm()

    return render(request, 'user/register.html', {'forms':form})

def LogoutView(request):
    logout(request)
    return redirect("login")

# Create your views here.
