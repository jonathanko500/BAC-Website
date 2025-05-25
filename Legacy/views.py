from django.shortcuts import render, redirect, get_object_or_404
from .models import Grad, agPolo_Record, AgeTeam

# Create your views here.


def agPolo_records_view(request):
    age_teams = AgeTeam.objects.all()
    context = {'age_teams': age_teams}
    return render(request, 'legacy/agPoloRecords.html', context)


def add_agPolo_records(request):
    if request.method == 'POST':
        age_of_team_name = request.POST['age_of_team']
        type_of_team = request.POST['type_of_team']
        tournament = request.POST['tournament']
        placement = request.POST['placement']
        season = request.POST['season']

        # Get or create the AgeTeam instance
        age_team, created = AgeTeam.objects.get_or_create(
            name=age_of_team_name)

        # Create and save a new agPolo_Record instance associated with the AgeTeam
        record = agPolo_Record(
            age_of_team=age_team, type_of_team=type_of_team,
            tournament=tournament, placement=placement, season=season)
        record.save()

        return redirect('legacy:agPolorecords')

    return render(request, 'legacy/agPoloRecords.html')


def delete_agPolo_record(request, record_id):
    record = agPolo_Record.objects.get(pk=record_id)
    record.delete()
    return redirect('legacy:agPolorecords')


def agPolo_alumni_view(request):
    grad = Grad.objects.all()
    return render(request, 'legacy/agPoloAlumni.html', {'grad': grad})


def add_grad_polo(request):
    if request.method == 'POST':
        grad_name = request.POST['grad_name']
        # Use FILES.get() to handle file upload
        picture = request.FILES.get('picture')

        # Perform any necessary validation here

        # Create and save Grad instance
        grad = Grad(  # make sure to change model for other database
            name=grad_name, picture=picture)
        grad.save()

        return redirect('legacy:agPoloalumni')

    return render(request, 'legacy/agPoloAlumni.html')

# delete coaches for grad polo


def delete_grad_polo(request, grad_name):
    mCoach = Grad.objects.get(pk=grad_name)
    mCoach.delete()
    return redirect('legacy:agPoloalumni')
