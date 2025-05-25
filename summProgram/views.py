from django.shortcuts import render, redirect, get_object_or_404
from .models import Program, Session, WeekendSession, PageInfo
from .forms import ProgramForm, SessionForm, WeekendSessionForm, PageInfoForm
from django.forms import inlineformset_factory
from datetime import datetime, timedelta

def summProgram_view(request):
    programs = Program.objects.all()
    page_info = PageInfo.objects.all()
    context = {
        'programs': programs,
        'page_info': page_info
    }
    return render(request, 'summProgram/summPage.html', context)

def add_program_and_sessions_view(request):
    SessionFormSet = inlineformset_factory(Program, Session, form=SessionForm, extra=1)
    WeekendSessionFormSet = inlineformset_factory(Program, WeekendSession, form=WeekendSessionForm, extra=1)
    
    if request.method == 'POST':
        program_form = ProgramForm(request.POST, request.FILES)
        session_formset = SessionFormSet(request.POST, request.FILES)
        weekend_session_formset = WeekendSessionFormSet(request.POST, request.FILES)
        
        if program_form.is_valid() and session_formset.is_valid() and weekend_session_formset.is_valid():
            program = program_form.save()
            session_formset.instance = program
            session_formset.save()
            weekend_session_formset.instance = program
            weekend_session_formset.save()
            
            start_date_str = request.POST.get('start_date')
            end_date_str = request.POST.get('end_date')
            weekend_start_date_str = request.POST.get('weekend_start_date')
            weekend_end_date_str = request.POST.get('weekend_end_date')
            if start_date_str and end_date_str:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                for i in range(program.number_of_sessions):
                    session_start_date = start_date + timedelta(weeks=i)
                    session_end_date = end_date + timedelta(weeks=i)
                    Session.objects.create(
                        program=program,
                        start_date=session_start_date,
                        end_date=session_end_date,
                        is_open=True
                    )
            if weekend_start_date_str and weekend_end_date_str:
                weekend_start_date = datetime.strptime(weekend_start_date_str, '%Y-%m-%d').date()
                weekend_end_date = datetime.strptime(weekend_end_date_str, '%Y-%m-%d').date()
                for i in range(program.number_of_weekend_sessions):
                    weekend_session_start_date = weekend_start_date + timedelta(weeks=i)
                    weekend_session_end_date = weekend_end_date + timedelta(weeks=i)
                    WeekendSession.objects.create(
                        program=program,
                        start_date=weekend_session_start_date,
                        end_date=weekend_session_end_date,
                        is_open=True
                    )
            return redirect('summProgram:summProgram')
    else:
        program_form = ProgramForm()
        session_formset = SessionFormSet()
        weekend_session_formset = WeekendSessionFormSet()
    
    context = {
        'program_form': program_form,
        'session_formset': session_formset,
        'weekend_session_formset': weekend_session_formset
    }
    return render(request, 'summProgram/addProgram.html', context)

def edit_program_view(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    SessionFormSet = inlineformset_factory(Program, Session, form=SessionForm, extra=0, can_delete=True)
    WeekendSessionFormSet = inlineformset_factory(Program, WeekendSession, form=WeekendSessionForm, extra=0, can_delete=True)
    
    if request.method == 'POST':
        program_form = ProgramForm(request.POST, request.FILES, instance=program)
        session_formset = SessionFormSet(request.POST, request.FILES, instance=program)
        weekend_session_formset = WeekendSessionFormSet(request.POST, request.FILES, instance=program)
        
        if program_form.is_valid() and session_formset.is_valid() and weekend_session_formset.is_valid():
            program_form.save()
            session_formset.save()
            weekend_session_formset.save()
            
            for form in session_formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    session = form.instance
                    session.is_open = form.cleaned_data['is_open']
                    session.start_date = form.cleaned_data['start_date']
                    session.end_date = form.cleaned_data['end_date']
                    session.save()
            
            for form in weekend_session_formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    weekend_session = form.instance
                    weekend_session.is_open = form.cleaned_data['is_open']
                    weekend_session.start_date = form.cleaned_data['start_date']
                    weekend_session.end_date = form.cleaned_data['end_date']
                    weekend_session.save()
            
            return redirect('summProgram:summProgram')
    else:
        program_form = ProgramForm(instance=program)
        session_formset = SessionFormSet(instance=program)
        weekend_session_formset = WeekendSessionFormSet(instance=program)
    
    context = {
        'program_form': program_form,
        'session_formset': session_formset,
        'weekend_session_formset': weekend_session_formset,
        'program': program
    }
    return render(request, 'summProgram/editProgram.html', context)

def delete_program_view(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    
    if request.method == 'POST':
        program.delete()
        return redirect('summProgram:summProgram')
    
    context = {
        'program': program
    }
    return render(request, 'summProgram/summPage.html', context)

def edit_page_info_view(request):
    page_info, created = PageInfo.objects.get_or_create(id=1)  # Use a specific ID, e.g., 1
    
    if request.method == 'POST':
        page_info_form = PageInfoForm(request.POST, request.FILES, instance=page_info)
        
        if page_info_form.is_valid():
            page_info_form.save()
            return redirect('summProgram:summProgram')
    else:
        page_info_form = PageInfoForm(instance=page_info)
    
    return render(request, 'summProgram/editPageInfo.html', {'page_info_form': page_info_form})
