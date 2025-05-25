"""
VIEWS FOR MASTERS
"""
from django.shortcuts import render, redirect
from .forms import ScheduleSwimForm, SchedulePoloForm
from .models import ScheduleSwim, SchedulePolo


def masters_swim_view(request):
    schedules = ScheduleSwim.objects.all()  # need this in all viewing page
    return render(request, 'masters/mastersSwim.html',  {'schedules': schedules})


def edit_swim_schedule(request):
    schedule, created = ScheduleSwim.objects.get_or_create(
        id=1)  # Use a specific ID, e.g., 1
    if request.method == 'POST':
        form = ScheduleSwimForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            # Redirect to the 'edit_schedule' URL
            return redirect('masters:mastersSwim')
    else:
        form = ScheduleSwimForm(instance=schedule)
    return render(request, 'masters/mastersSwim_edit_schedule.html', {'form': form})


def masters_polo_view(request):
    schedules = SchedulePolo.objects.all()  # need this in all viewing page
    return render(request, 'masters/mastersPolo.html',  {'schedules': schedules})


def edit_polo_schedule(request):
    schedule, created = SchedulePolo.objects.get_or_create(
        id=1)  # Use a specific ID, e.g., 1
    if request.method == 'POST':
        form = SchedulePoloForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            # Redirect to the 'edit_schedule' URL
            return redirect('masters:mastersPolo')
    else:
        form = SchedulePoloForm(instance=schedule)
    return render(request, 'masters/mastersPolo_edit_schedule.html', {'form': form})
