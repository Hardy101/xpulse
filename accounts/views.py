from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import AccountCreationForm, CustomLoginForm
from .backends import EmailBackend

# Create your views here.
def register(request): 
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user) 
            return redirect('home')  # Redirect to a success page
    else:
        form = AccountCreationForm()
    return render(request, 'pages/register.html', {'form': form})


def login_view(request): 
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user:
                login(request, user)  # Log in the user
                return redirect('home')  # Replace 'home' with your desired page
            else:
                form.add_error('email', 'No account found with that email.')
    else:
        form = CustomLoginForm()

    return render(request, 'pages/login.html', {'form': form})


def logout_view(request):
  logout(request)
  return redirect('register') 