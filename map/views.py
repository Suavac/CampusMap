from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .forms import CourseForm, ModuleForm, RoomForm, LecturerForm, BuildingForm, TimetableForm, DepartmentForm

from .models import Course, Timetable, Building, Module, Lecturer, Department, TimeEntry
from django.shortcuts import render_to_response
from django.template import RequestContext

import json

def editTimetable(request):

    check = "false"

    if request.method == 'POST': # If the form has been submitted...
        form = TimetableForm(request.POST) # A form bound to the POST data

        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            save_it = form.save()
            save_it.save()

            check = "true"

            #return HttpResponseRedirect('/editTimetable/',
             #                           {'check' : check,
              #                           'course' : form.courseCode}) # Redirect after POST
    else:
        form = TimetableForm() # An unbound form

    return render(request, 'timetable.html', {
        'form': form,
        'check': check
    })

def editMap(request):
    return render(request, 'map.html')


# Handle JSON requests
def JSON(request):

    message = request.GET.get('message')
    print message

    d = Department.objects.all()
    c = Course.objects.all()
    exists = False

    # returns list of available courses
    if (message == 'courses'):

        temp = []

        for o in c.iterator():

            temp.append(o.courseCode)

        data = {'courses' : temp}

        return JsonResponse(data)


    elif (message == 'departments'):
        temp = []


        for dept in d.iterator():
            temp2 = []
            temp2.append(dept.depName)
            temp2.append(dept.depShort)
            temp.append(temp2)

            print temp
        data = {'departments' : temp}
        #print data

        return JsonResponse(data)

    elif (message == 'Arts' or message == 'Engineering' or message == 'Medicine' or message == 'Business' or message == 'Science'):
        courses = []

        for f in c.iterator():
            if f.department.depShort == message:

                courses.append(f.courseCode)
                print('match')

        print courses
        data = {'courses' : courses}

        return JsonResponse(data)

    # checks for queried course
    for o in c.iterator():
        if message == o.courseCode:
            exists = True

    if (exists):

        course = Course.objects.get(courseCode=message)

        timetable = []

        t = Timetable.objects.filter(courseCode=Course.objects.get(courseCode=message))

        for o in t.iterator():

            tempData = {
            'mod' : o.modCode.modCode,
            'room' : o.roomCode.roomCode,
            'lec' : o.lecCode.lecFirst_Name + " " + o.lecCode.lecLast_Name,
            'day' : o.day,
            'time' : o.time
            }

            tempData2json = json.dumps(tempData)

            timetable.append(tempData)

        #temp2json = json.dumps(timetable)

        data = {'code' : message, 'title' : course.courseName, 'department'  : course.department.depName,
        'timetable' : timetable}


        return JsonResponse(data)

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
