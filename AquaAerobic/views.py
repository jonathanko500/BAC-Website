"""
URL FOR AQUA AEROBIC
"""

from django.shortcuts import render, redirect
from .forms import ScheduleForm
from .models import Schedule


def index(request):
    schedules = Schedule.objects.all()  # need this in all viewing page
    return render(request, 'aquaaerobic/aquaaerobic.html', {'schedules': schedules})


def edit_schedule(request):
    schedule, created = Schedule.objects.get_or_create(
        id=1)  # Use a specific ID, e.g., 1
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            # Redirect to the 'edit_schedule' URL
            return redirect('aquaaerobic:index')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'aquaaerobic/edit_schedule.html', {'form': form})
