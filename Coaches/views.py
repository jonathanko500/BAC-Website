"""
VIEWS FOR COACHES
"""

from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .models import Coach, mCoachSwim, compCoachPolo, compCoachSwim

# views coaches for masters swim


def masters_swim_coaches_view(request):
    coaches = mCoachSwim.objects.all()  # Use mCoachSwim instead of Coach
    return render(request, 'coaches/mastersSwimCoaches.html', {'coaches': coaches})

# add coaches for masters swim


def add_coach_swim(request):
    if request.method == 'POST':
        coach_name = request.POST['coach_name']
        description = mark_safe(request.POST['description'])
        # Use FILES.get() to handle file upload
        picture = request.FILES.get('picture')

        # Perform any necessary validation here

        # Create and save Coach instance
        coach = mCoachSwim(  # make sure to change model for other database
            name=coach_name, description=description, picture=picture)
        coach.save()

        return redirect('coaches:mastersSwimCoaches')

    return render(request, 'coaches/add_coach_swim.html')

# delete coaches for masters swim


def delete_coach_swim(request, coach_name):
    mCoach = mCoachSwim.objects.get(pk=coach_name)
    mCoach.delete()
    return redirect('coaches:mastersSwimCoaches')

# views coaches for masters polo


def masters_polo_coaches_view(request):
    coaches = Coach.objects.all()
    context = {'coaches': coaches}
    return render(request, 'coaches/mastersPoloCoaches.html', context)

# add coaches for masters polo


def add_coach(request):
    if request.method == 'POST':
        coach_name = request.POST['coach_name']
        description = mark_safe(request.POST['description']) 
        # Use FILES.get() to handle file upload
        picture = request.FILES.get('picture')

        # Perform any necessary validation here

        # Create and save Coach instance
        coach = Coach(name=coach_name,
                      description=description, picture=picture)
        coach.save()

        return redirect('coaches:mastersPoloCoaches')

    return render(request, 'coaches/add_coach.html')

# delete coaches for masters polo


def delete_coach_polo(request, coach_name):
    mpCoach = Coach.objects.get(pk=coach_name)
    mpCoach.delete()
    return redirect('coaches:mastersPoloCoaches')

# views coaches for AG polo


def AG_polo_coaches_view(request):
    coaches = compCoachPolo.objects.all()
    return render(request, 'coaches/agPoloCoaches.html', {'coaches': coaches})

# add coaches for AG polo


def add_AG_polo_coaches(request):
    if request.method == 'POST':
        coach_name = request.POST['coach_name']
        description = mark_safe(request.POST['description']) 
        # Use FILES.get() to handle file upload
        picture = request.FILES.get('picture')

        # Perform any necessary validation here

        # Create and save Coach instance
        coach = compCoachPolo(name=coach_name,
                              description=description, picture=picture)
        coach.save()

        return redirect('coaches:AGPoloCoaches')

    return render(request, 'coaches/add_coach.html')

# delete coaches for AG polo


def delete_AG_polo_coaches(request, coach_name):
    agpCoach = compCoachPolo.objects.get(pk=coach_name)
    agpCoach.delete()
    return redirect('coaches:AGPoloCoaches')


# views coaches for AG polo
def AG_swim_coaches_view(request):
    coaches = compCoachSwim.objects.all()
    return render(request, 'coaches/agSwimCoaches.html', {'coaches': coaches})

# add coaches for AG polo


def add_AG_swim_coaches(request):
    if request.method == 'POST':
        coach_name = request.POST['coach_name']
        coach_title = request.POST['coach_title']
        description = mark_safe(request.POST['description']) 
        # Use FILES.get() to handle file upload
        picture = request.FILES.get('picture')

        # Perform any necessary validation here

        # Create and save Coach instance
        coach = compCoachSwim(name=coach_name,coaches_title = coach_title,
                              description=description, picture=picture)
        coach.save()

        return redirect('coaches:AGSwimCoaches')

    return render(request, 'coaches/add_coach.html')

# delete coaches for AG polo


def delete_AG_swim_coaches(request, coach_name):
    agpCoach = compCoachSwim.objects.get(pk=coach_name)
    agpCoach.delete()
    return redirect('coaches:AGSwimCoaches')