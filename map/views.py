from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CourseForm, ModuleForm, RoomForm, LecturerForm, BuildingForm,TimetableForm
import json
from .models import Course, Timetable

def editTimetable(request):
    return render(request, 'timetable.html')

## Testing JSON responses
def detail(request):

    message = request.GET.get('message')

    course = Course.objects.get(courseCode=message) #objects.all().filter(courseCode=message)

    temp = []

    t = Timetable.objects.filter(courseCode=Course.objects.get(courseCode=message))

    for o in t.iterator():

        tempData = {
        'code' : o.courseCode.courseCode,
        'mod' : o.modCode.modCode,
        'room' : o.roomCode.roomCode,
        'lec' : o.lecCode.lecFirst_Name + " " + o.lecCode.lecLast_Name,
        'day' : o.day,
        'time' : o.time
        }

        temp.append(tempData)

    temp2json = json.dumps(temp)

    data = {'code' : message, 'title' : course.courseName, 'department' : course.department,
    'timetable' : temp2json}

    json_data = json.dumps(data)

    return render(request, 'test.html', {"foo": json_data})

def home(request):
    return render(request, 'home.html')

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

    return render(request, 'dbstuff/addcourse.html', {
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

    return render(request, 'dbstuff/addmodule.html', {
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

    return render(request, 'dbstuff/addroom.html', {
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

    return render(request, 'dbstuff/addlecturer.html', {
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
            return HttpResponseRedirect('/building/') # Redirect after POST
    else:
        form = BuildingForm() # An unbound form

    return render(request, 'dbstuff/addbuilding.html', {
        'form': form,
    })

def timetable(request):
    if request.method == 'POST': # If the form has been submitted...
        form = TimetableForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            save_it = form.save()
            save_it.save()
            return HttpResponseRedirect('/timetable/') # Redirect after POST
    else:
        form = TimetableForm() # An unbound form

    return render(request, 'dbstuff/addtimetable.html', {
        'form': form,
    })

