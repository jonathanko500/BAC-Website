from django.shortcuts import render, get_object_or_404, redirect
from .models import Holiday
from .forms import HolidayForm

def holiday_view(request):
    holidays = Holiday.objects.all()
    return render(request, 'holiday/holiday.html', {'holidays': holidays})

def create_holidays_view(request):
    if request.method == 'POST':
        form = HolidayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('holiday:holiday_view')  
    else:
        form = HolidayForm()
    return render(request, 'holiday/add_holiday.html', {'form': form})

def edit_holiday_view(request, pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    if request.method == 'POST':
        form = HolidayForm(request.POST, instance=holiday)
        if form.is_valid():
            form.save()
            return redirect('holiday:holiday_view')  
    else:
        form = HolidayForm(instance=holiday)
    return render(request, 'holiday/edit_holiday.html', {'form': form})


def delete_holiday_view(request, pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    if request.method == 'POST':
        holiday.delete()
        return redirect('holiday:holiday_view')
    return render(request, 'holiday/delete_holiday.html', {'holiday': holiday})    