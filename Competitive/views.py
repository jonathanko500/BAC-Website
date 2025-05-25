"""
VIEWS FOR COMP
"""

from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import AGswimPageForm, AGpoloPageForm
from .models import AGswimPage, AGpoloPage, AGswimEmail, AGpoloEmail


def comp_swim_view(request):
    schedules = AGswimPage.objects.all()
    emails = AGswimEmail.objects.all()

    context = {
        'schedules': schedules,
        'emails': emails,
    }

    return render(request, 'competitive/competitiveSwim.html', context)


def edit_comp_swim(request):
    schedule, created = AGswimPage.objects.get_or_create(
        id=1)  # Use a specific ID, e.g., 1
    if request.method == 'POST':
        form = AGswimPageForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            # Redirect to the 'edit_schedule' URL
            return redirect('competitive:compSwim')
    else:
        form = AGswimPageForm(instance=schedule)
    return render(request, 'competitive/agSwimEdit.html', {'form': form})


def upload_pdf_swim(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        title = request.POST['title']
        pdf_file = request.FILES['pdf_file']
        uploaded_pdf = AGswimEmail(title=title, pdf_file=pdf_file)
        uploaded_pdf.save()
        # Redirect to a list view of uploaded PDFs
        return redirect('competitive:compSwim')

    return render(request, 'competitive/competitiveSwim.html')


def download_pdf_swim(request, pdf_id):
    try:
        pdf = AGswimEmail.objects.get(id=pdf_id)
    except AGswimEmail.DoesNotExist:
        # Handle the case where the PDF doesn't exist
        pass
    else:
        # Generate a response to download the PDF
        response = FileResponse(pdf.pdf_file, as_attachment=True)
        return response


def comp_polo_view(request):
    schedules = AGpoloPage.objects.all()
    emails = AGpoloEmail.objects.all()

    context = {
        'schedules': schedules,
        'emails': emails,
    }
    return render(request, 'competitive/competitivePolo.html', context)


def edit_comp_polo(request):
    schedule, created = AGpoloPage.objects.get_or_create(
        id=1)  # Use a specific ID, e.g., 1
    if request.method == 'POST':
        form = AGpoloPageForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            # Redirect to the 'edit_schedule' URL
            return redirect('competitive:compPolo')
    else:
        form = AGpoloPageForm(instance=schedule)
    return render(request, 'competitive/agPoloEdit.html', {'form': form})


def upload_pdf_polo(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        title = request.POST['title']
        pdf_file = request.FILES['pdf_file']
        uploaded_pdf = AGpoloEmail(title=title, pdf_file=pdf_file)
        uploaded_pdf.save()
        # Redirect to a list view of uploaded PDFs
        return redirect('competitive:compPolo')

    return render(request, 'competitive/competitivePolo.html')


def download_pdf_polo(request, pdf_id):
    try:
        pdf = AGpoloEmail.objects.get(id=pdf_id)
    except AGpoloEmail.DoesNotExist:
        # Handle the case where the PDF doesn't exist
        pass
    else:
        # Generate a response to download the PDF
        response = FileResponse(pdf.pdf_file, as_attachment=True)
        return response