from django.shortcuts import render, redirect
from .forms import homePageForm
from .models import homePage as HomePageModel

def index(request):
    homepages = HomePageModel.objects.all()  # Use a different variable name
    return render(request, 'home/home.html', {'homepages': homepages})

def edit_homePage(request):
    schedule, created = HomePageModel.objects.get_or_create(id=1)
    
    if request.method == 'POST':
        home_form = homePageForm(request.POST, request.FILES, instance=schedule)
        
        if home_form.is_valid():
            home_form.save()
            return redirect('index')
    else:
        home_form = homePageForm(instance=schedule)
    
    return render(request, 'home/edit_home.html', {'home_form': home_form})
