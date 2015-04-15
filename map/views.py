from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import CourseForm, ModuleForm, RoomForm, LecturerForm, BuildingForm, TimetableForm, DepartmentForm

from .models import Course, Timetable, Building, Module, Lecturer, Department, TimeEntry, Room
from django.shortcuts import render_to_response
from django.template import RequestContext


import json, urllib, urlparse

def editTimetable(request):

    check = "false"

    if request.method == 'POST': # If the form has been submitted...
        form = TimetableForm(request.POST) # A form bound to the POST data

        if form.is_valid():
            save_it = form.save()
            save_it.save()
            check = "true"
    else:
        form = TimetableForm() # An unbound form

    return render(request, 'timetable.html', {
        'form': form,
        'check': check
    })





def editMap(request):

    return render(request, 'map.html')


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


# Handle JSON requests
def JSON(request):

    message = urllib.unquote(request.get_full_path()).split('/json/?message=') # Gets JSON message
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


    elif (submessage[0] == 'departments'):
        temp = []

        for dept in d.iterator():
            temp.append(dept.depName)

        data = {'departments' : temp}

        return JsonResponse(data)


    elif (submessage[0] == 'years'):
        temp = []
        for o in t.iterator():
            if course == o.courseCode.courseCode and o.semester == '1':
                temp.append(o.courseCode.courseCode)

        data = {'years' : temp}

        return JsonResponse(data)


    elif (submessage[0] == 'load'):
        # checks for queried course
        for o in c.iterator():
            if course == o.courseCode:
                exists = True

        if (exists):

            cs = Course.objects.get(courseCode=course)

            timetable = []

            t = TimeEntry.objects.filter(timeTable=Timetable.objects.get(courseCode=cs,year=year,semester=semester)) #filters out desired timetable

            for o in t.iterator():

                tempData = {
                    'mod' : o.modCode.modCode,
                    'room' : o.roomCode.roomCode,
                    'lec' : o.lecCode.lecFirst_Name + " " + o.lecCode.lecLast_Name,
                    'day' : o.day,
                    'time' : o.time,
                    'colour' : o.modCode.color.hex
                }

                #tempData2json = json.dumps(tempData)

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
            return JsonResponse({'Course Not Found' : 'null'})

    else:
        return JsonResponse({'Invalid Query' : 'null'})


def home(request):
    return render(request, 'home.html')

def course(request):
    # get all data from course table in ascending order
    query_results = Course.objects.all().order_by('courseCode')
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
     # get all data from lecturer table in ascending order
    query_results = Lecturer.objects.all()
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


def building(request):
    # get all data from building table in ascending order
    query_results = Building.objects.all().order_by('buildingName')

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

def department(request):
    # get all data from building table in ascending order
    query_results = Department.objects.all()

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
