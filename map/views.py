from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CourseForm, ModuleForm, RoomForm, LecturerForm, BuildingForm

def home(request):
    return render(request, 'home.html')

def timetable(request):
    return render(request, 'timetable.html')

def course(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CourseForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            save_it = form.save()
            save_it.save()
            return HttpResponseRedirect('/course/') # Redirect after POST
    else:
        form = CourseForm() # An unbound form

    return render(request, 'dbstaff/addcourse.html', {
        'form': form,
    })

def module(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ModuleForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            save_it = form.save()
            save_it.save()
            return HttpResponseRedirect('/module/') # Redirect after POST
    else:
        form = ModuleForm() # An unbound form

    return render(request, 'dbstaff/addmodule.html', {
        'form': form,
    })

def room(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RoomForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            save_it = form.save()
            save_it.save()
            return HttpResponseRedirect('/room/') # Redirect after POST
    else:
        form = RoomForm() # An unbound form

    return render(request, 'dbstaff/addroom.html', {
        'form': form,
    })

def lecturer(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LecturerForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            save_it = form.save()
            save_it.save()
            return HttpResponseRedirect('/lecturer/') # Redirect after POST
    else:
        form = LecturerForm() # An unbound form

    return render(request, 'dbstaff/addroom.html', {
        'form': form,
    })

def building(request):
    if request.method == 'POST': # If the form has been submitted...
        form = BuildingForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            save_it = form.save()
            save_it.save()
            return HttpResponseRedirect('/lecturer/') # Redirect after POST
    else:
        form = BuildingForm() # An unbound form

    return render(request, 'dbstaff/addbuilding.html', {
        'form': form,
    })

