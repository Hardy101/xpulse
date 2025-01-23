from django.shortcuts import render, redirect
from .forms import AccountCreationForm

# Create your views here.
def register(request): 
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = AccountCreationForm()
    return render(request, 'pages/register.html', {'form': form})
