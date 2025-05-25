"""
VIEWS FOR ABOUTUS
"""
from django.shortcuts import render, redirect, get_object_or_404
from .forms import aboutusEditForm
from .models import aboutusEdit, jobDesc


# about us page
def aboutus_view(request):
    change = aboutusEdit.objects.all()
    return render(request, 'AboutUs/aboutus.html', {'change': change})


def edit_aboutus(request):
    schedule, created = aboutusEdit.objects.get_or_create(
        id=1)  # Use a specific ID, e.g., 1
    if request.method == 'POST':
        form = aboutusEditForm(request.POST, request.FILES, instance=schedule)
        if form.is_valid():
            form.save()
            # Redirect to the 'edit_schedule' URL
            return redirect('aboutus:aboutus')
    else:
        form = aboutusEditForm(instance=schedule)
    return render(request, 'AboutUs/edit_aboutus.html', {'form': form})


# job desc page
def jobDesc_view(request):
    change = jobDesc.objects.all()
    return render(request, 'AboutUs/jobsDesc.html', {'change': change})


def jobDesc_create_view(request):
    if request.method == 'POST':
        job_name = request.POST.get('name')
        job_type = request.POST.get('job_type')
        job_description_file = request.FILES.get('jobDesc_file')

        # Perform any necessary validation here
        if job_name and job_type and job_description_file:
            # Create and save jobDesc instance
            job_description = jobDesc(
                name=job_name,
                job_type=job_type,
                jobDesc_file=job_description_file
            )
            job_description.save()

            return redirect('aboutus:jobDesc')
        else:
            # Handle the case where validation fails
            return render(request, 'AboutUs/jobsDesc.html', {'error': 'All fields are required.'})

    return render(request, 'AboutUs/jobsDesc.html')


def delete_job_desc(request, job_id):
    job_description = get_object_or_404(jobDesc, id=job_id)

    if request.method == 'POST':
        job_description.delete()
        return redirect('aboutus:jobDesc')

    return render(request, 'AboutUs/jobsDesc.html', {'job_description': job_description})
