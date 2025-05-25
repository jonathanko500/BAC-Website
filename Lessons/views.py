"""
VIEWS FOR LESSONS
"""
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .forms import PrivateScheduleForm, Swim_LessonForm, lessonInfoHomeForm, Group_Lesson_InfoForm
from .models import PrivateSchedule, SwimLessons, lessonInfoHome, Group_Lesson_Info

# home swim lesson page


def swim_lessons(request):
    schedules = SwimLessons.objects.all()
    return render(request, 'lessons/lessonHome.html', {'schedules': schedules})

# lesson desc page


def lessonInfoHome_view(request):
    schedules = lessonInfoHome.objects.all()
    info = Group_Lesson_Info.objects.all().order_by('level')

    context = {
        'schedules': schedules,
        'info': info
    }

    return render(request, 'lessons/lessonInfo.html', context)

# private lesson page


def private_view(request):
    schedules = PrivateSchedule.objects.all()
    return render(request, 'lessons/private.html', {'schedules': schedules})

# edit home swim lesson page


def edit_swim_lessons(request):
    schedule, created = SwimLessons.objects.get_or_create(
        id=1)  # Use a specific ID, e.g., 1
    if request.method == 'POST':
        form = Swim_LessonForm(request.POST, request.FILES, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('lessons:swim_lessons')
    else:
        form = Swim_LessonForm(instance=schedule)
    return render(request, 'lessons/edit_lessonHome.html', {'form': form})

# edit lesson desc page


def edit_lessonInfoHome_view(request):  # edit lesson info page
    group_detail_instance, created = lessonInfoHome.objects.get_or_create(
        id=1)  # Use a specific ID, e.g., 1
    if request.method == 'POST':
        form = lessonInfoHomeForm(
            request.POST, instance=group_detail_instance)
        if form.is_valid():
            form.save()
            # Redirect to the 'edit_group_detail' URL
            return redirect('lessons:lessonInfo')
    else:
        form = lessonInfoHomeForm(instance=group_detail_instance)
    return render(request, 'lessons/edit_lessonInfo.html', {'form': form})


def edit_GroupDetailInfo_view(request):  # add lesson info "cards"
    if request.method == 'POST':
        form = Group_Lesson_InfoForm(
            request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to the 'edit_group_detail' URL
            return redirect('lessons:lessonInfo')
    else:
        form = Group_Lesson_InfoForm()
    return render(request, 'lessons/lessonInfo_adder.html', {'form': form})


class GroupLessonInfoDeleteView(DeleteView): # delete lesson info "cards"
    model = Group_Lesson_Info
    # Adjust the URL name as needed
    success_url = reverse_lazy('lessons:lessonInfo')

    # Optional: If you want to add any specific logic before or after deletion, override the delete method.
    def delete(self, request, *args, **kwargs):
        # Custom logic here (if needed)
        return super(GroupLessonInfoDeleteView, self).delete(request, *args, **kwargs)

# edit private lesson page


def edit_private(request):
    private_instance, created = PrivateSchedule.objects.get_or_create(
        id=1)  # Use a specific ID, e.g., 1
    if request.method == 'POST':
        form = PrivateScheduleForm(
            request.POST, instance=private_instance)
        if form.is_valid():
            form.save()
            # Redirect to the 'edit_group_detail' URL
            return redirect('lessons:private')
    else:
        form = PrivateScheduleForm(instance=private_instance)
    return render(request, 'lessons/edit_private.html', {'form': form})
