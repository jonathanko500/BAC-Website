from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Call form.save() to save the user
            
            # After saving the user, you can authenticate and log in the user if needed
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)

            return redirect('index')  
    else:
        form = RegisterForm()
    
    return render(request, "register/register.html", {"form": form})
