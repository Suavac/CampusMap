from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import CourseForm, ModuleForm, RoomForm, LecturerForm, BuildingForm, TimetableForm, DepartmentForm,TimeEntryForm

from .models import Course, Timetable, Building, Module, Lecturer, Department, TimeEntry, Room
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.core.context_processors import csrf
from django.contrib import  auth

import json, urllib, urlparse

from django.contrib.auth.decorators import login_required


def login(request):
    c = {} # create dict
    c.update(csrf(request)) # push csrf object to it

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/home/') # Redirect after POST
    else:
        return HttpResponseRedirect('/home/') # Redirect after POST

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/') # Redirect after POST


@login_required
def editTimetable(request):

    #Variables that are sent back to timetable.html to reload timetable after post
    check = 'false'
    c = 'null'
    y = 'null'
    s = 'null'

    if request.method == 'POST': # If the form has been submitted...
        form = TimeEntryForm(request.POST) # A form bound to the POST data

        if form.is_valid():
            save_it = form.save()
            save_it.save()

            #gets timeTable object from database and extracts course, year and semester values from it
            id = request.POST.get('timeTable','')
            t = Timetable.objects.all().get(id=id)
            t = str(t)
            t = t.split(' ')
            c = t[0]
            y = t[1].split('year:')[1]
            s = t[2].split('sem:')[1]
            check = 'true'
    else:
        form = TimeEntryForm() # An unbound form

    return render(request, 'timetable.html', {
        'form': form,
        'check': check,
        'course': c,
        'year': y,
        'sem': s
    })


def editMapJson(request):

    message = request.GET.get('message')

    if (message == 'buildings'):

        b = Building.objects.all()

        temp = []

        for o in b.iterator():
            temp.append(o.buildingName)
        data = {'buildings' : temp}

        return JsonResponse(data)

    elif (message == 'rooms'):

        print message

        r = Room.objects.all()
        b = request.GET.get('building')

        temp = []
        for o in r.iterator():
            if o.building.buildingName == b:
                temp.append(o.roomCode)

        data = {'rooms' : temp}

        print data

        return JsonResponse(data)

    elif (message == 'coord'):

        room = request.GET.get('room')

        r = Room.objects.get(roomCode=room)

        print r.lat

        data = {'lat' : r.lat, 'lng' : r.lng}

        return JsonResponse(data)

    elif (message == 'newCoord'):

        try:
            room = request.GET.get('room')
            r = Room.objects.get(roomCode=room)
            print str(request.GET.get('lat'))
            r.lat = float(request.GET.get('lat'))
            r.lng = float(request.GET.get('lng'))
            r.save()
            response = HttpResponse("success")
        except Exception:
            response = HttpResponse("failed")

        return response

    else:

        return HttpResponse("Invalid Query")


# Handles JSON requests
def JSON(request):

    message = urllib.unquote(request.get_full_path()).split('/json/?message=') # Gets JSON message sent from webpage
    #Splits message into parts
    submessage = message[1].split('&')
    dept = submessage[1].split('department=')[1]
    course = submessage[2].split('course=')[1]
    year = submessage[3].split('year=')[1]
    semester = submessage[4].split('semester=')[1]

    d = Department.objects.all()
    c = Course.objects.all()
    t = Timetable.objects.all()

    exists = False

    # returns list of available courses
    if (submessage[0] == 'courses'):
        temp = []

        for o in c.iterator():
            if o.department.depName == dept:
                temp.append(o.courseCode)

        data = {'courses' : temp}

        return JsonResponse(data)

    #returns a list of available departments
    elif (submessage[0] == 'departments'):
        temp = []

        for dept in d.iterator():
            temp.append(dept.depName)

        data = {'departments' : temp}

        return JsonResponse(data)

    #returns course codes for year filtering in timetable.html
    elif (submessage[0] == 'years'):
        temp = []
        for o in t.iterator():
            if course == o.courseCode.courseCode and o.semester == '1':
                temp.append(o.courseCode.courseCode)

        data = {'years' : temp}

        return JsonResponse(data)

    #loads timetable
    elif (submessage[0] == 'load'):
        # checks for queried course
        for o in c.iterator():
            if course == o.courseCode:
                exists = True

        if (exists):

            cs = Course.objects.get(courseCode=course)

            timetable = []

            t = TimeEntry.objects.filter(timeTable=Timetable.objects.get(courseCode=cs,year=year,semester=semester)) #filters out desired timetable using variables obtained from JSON message

            for o in t.iterator():

                tempData = {
                    'mod' : o.modCode.modCode,
                    'room' : o.roomCode.roomName,
                    'lec' : o.lecCode.lecFirst_Name + " " + o.lecCode.lecLast_Name,
                    'day' : o.day,
                    'time' : o.time,
                    'colour' : o.modCode.color.hex
                }

                timetable.append(tempData)

            data = {
                'code' : message,
                'title' : cs.courseName,
                'year':year,
                'semester':semester,
                'department' : cs.department.depName,
                'timetable' : timetable
            }

            return JsonResponse(data)

        else:
            return JsonResponse({'Timetable Not Found' : 'null'})

    else:
        return JsonResponse({'Invalid Query' : 'null'})


def home(request):

    check = 'false'
    c = 'null'
    y = 'null'
    s = 'null'

    if request.method == 'POST': # If the form has been submitted...
        form = TimeEntryForm(request.POST) # A form bound to the POST data

        if form.is_valid():
            save_it = form.save()
            save_it.save()

            id = request.POST.get('timeTable','')
            t = Timetable.objects.all().get(id=id)
            tt = str(t)
            ttt = tt.split(' ')
            c = ttt[0]
            y = ttt[1].split('year:')[1]
            s = ttt[2].split('sem:')[1]
            check = 'true'
    else:
        form = TimeEntryForm() # An unbound form

    return render(request, 'home.html', {
        'form': form,
        'check': check,
        'course': c,
        'year':y,
        'sem':s
    })

@login_required
def course(request):
    # get all data from course table in ascending order
    query_results = Course.objects.all().order_by('courseCode')

    if request.method == 'GET':
        message = request.GET.get('message')

        if message == 'delete':
            record = request.GET.get('toDelete')
            Course.objects.filter(courseCode=record).delete()
            #return HttpResponseRedirect('/timetable/')

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

    return render_to_response('dbstuff/addcourse.html', locals(),context_instance=RequestContext(request))

@login_required
def module(request):
    # get all data from module table in ascending order
    query_results = Module.objects.all().order_by('modCode')

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

    return render_to_response('dbstuff/addmodule.html', locals(),context_instance=RequestContext(request))

@login_requiredp
def room(request):
    query_results = Room.objects.all().order_by('roomCode', 'building')

    if request.method == 'GET':
        message = request.GET.get('message')

        if message == 'delete':
            record = request.GET.get('toDelete')
            Room.objects.filter(roomCode=record).delete()
            #return HttpResponseRedirect('/timetable/')

    if request.method == 'POST': # If the form has been submitted...
        form = RoomForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            save_it = form.save()
            save_it.save()
            return HttpResponseRedirect('/rooms/') # Redirect after POST
    else:
        form = RoomForm() # An unbound form

    return render(request, 'dbstuff/addroom.html', locals(),context_instance=RequestContext(request))

@login_required
def lecturer(request):
     # get all data from lecturer table in ascending order
    query_results = Lecturer.objects.all()

    if request.method == 'GET':
        message = request.GET.get('message')

        if message == 'delete':
            record = request.GET.get('toDelete')
            Lecturer.objects.filter(lecCode=record).delete()
            #return HttpResponseRedirect('/timetable/')

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

    return render_to_response('dbstuff/addlecturer.html', locals(),context_instance=RequestContext(request))

@login_required
def building(request):
    # get all data from building table in ascending order
    query_results = Building.objects.all().order_by('buildingName')

    if request.method == 'GET':
        message = request.GET.get('message')

        if message == 'delete':
            record = request.GET.get('toDelete')
            Building.objects.filter(buildingName=record).delete()
            #return HttpResponseRedirect('/timetable/')

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

    return render_to_response('dbstuff/addbuilding.html', locals(),context_instance=RequestContext(request))

@login_required
def department(request):
    # get all data from building table in ascending order
    query_results = Department.objects.all().order_by('depName')

    if request.method == 'GET':
        message = request.GET.get('message')

        if message == 'delete':
            record = request.GET.get('toDelete')
            Department.objects.filter(depName=record).delete()
            #return HttpResponseRedirect('/timetable/')

    if request.method == 'POST': # If the form has been submitted...
        form = DepartmentForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            save_it = form.save()
            save_it.save()
            return HttpResponseRedirect('/department/') # Redirect after POST
    else:
        form = DepartmentForm() # An unbound form
    return render_to_response('dbstuff/adddepartment.html', locals(),context_instance=RequestContext(request))

@login_required
def timetable(request):
    # get all data from timetable table in ascending order
    query_results = Timetable.objects.all().order_by('courseCode', 'year', 'semester')

    if request.method == 'GET':
        message = request.GET.get('message')

        if message == 'delete':
            cc = request.GET.get('course')
            yr = request.GET.get('year')
            sr = request.GET.get('semester')
            Timetable.objects.filter(courseCode=cc, year=yr, semester=sr).delete()
            #return HttpResponseRedirect('/timetable/')

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

    return render(request, 'dbstuff/addtimetable.html', locals(),context_instance=RequestContext(request))
