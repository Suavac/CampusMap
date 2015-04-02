from django import forms
from django.template.defaultfilters import mark_safe

from .models import Course, Module, Lecturer, Room, Building, Timetable, Department, TimeEntry

class DepartmentForm(forms.ModelForm):

    depName = forms.CharField(max_length = 50,label = mark_safe('<strong>Department Name</strong>'))

    class Meta:
        model = Department

class CourseForm(forms.ModelForm):

    courseCode = forms.CharField(max_length=15,label = mark_safe('<strong>Code</strong>'))
    courseName = forms.CharField(max_length=50,label = mark_safe('<strong>Name</strong>'))
    department = queryset=Department.objects.all()

    class Meta:
        model = Course

class ModuleForm(forms.ModelForm):

    modCode = forms.CharField(max_length=7, label = mark_safe('<strong>Module Code</strong>'))
    modName = forms.CharField(max_length=70,label = mark_safe('<strong>Module Name</strong>'))

    class Meta:
        model = Module

class BuildingForm(forms.ModelForm):

    buildingName = forms.CharField(max_length = 75,label = mark_safe('<strong>Building Name</strong>'))

    class Meta:
        model = Building

class RoomForm(forms.ModelForm):

    roomCode = forms.CharField(max_length = 15,label = mark_safe('<strong>Room Code</strong>'))
    roomName = forms.CharField(max_length = 30,label = mark_safe('<strong>Room Name</strong>'))
    building = queryset=Building.objects.all()
    lat = forms.CharField(max_length = 9, label = mark_safe('<strong>Latitude</strong>'))
    lon = forms.CharField(max_length = 9, label = mark_safe('<strong>Longitude</strong>'))

    class Meta:
        model = Room



class LecturerForm(forms.ModelForm):

    lecCode = forms.CharField(max_length = 7,label = mark_safe('<strong>Code</strong>'),)
    lecFirst_Name = forms.CharField(max_length = 50,label = mark_safe('<strong>First Name</strong>'))
    lecLast_Name = forms.CharField(max_length = 50,label = mark_safe('<strong>Last Name</strong>'))
    lecEmail = forms.EmailField(label = mark_safe('<strong>Email</strong>'))
    class Meta:
        model = Lecturer



class TimetableForm(forms.ModelForm):

    courseCode = Course.objects.all()
    year = forms.CharField(max_length = 1)
    semester = forms.CharField(max_length = 1)
    #modCode = Module.objects.all()
    #roomCode = Room.objects.all()
    #lecCode = Lecturer.objects.all()

    #day = forms.CharField(max_length = 1)
    #time = forms.CharField(max_length = 2)

    #day = forms.ChoiceField(Timetable.DAY_CHOICES)
    #time = forms.ChoiceField(Timetable.HOURS_CHOICES)
    class Meta:
        model = Timetable

class TimeEntry(forms.ModelForm):

    timeTable = Timetable.objects.all()
    modCode = Module.objects.all()
    roomCode = Room.objects.all()
    lecCode = Lecturer.objects.all()
    day = forms.CharField(max_length = 1)
    time = forms.CharField(max_length = 2)

    #day = forms.ChoiceField(Timetable.DAY_CHOICES)
    #time = forms.ChoiceField(Timetable.HOURS_CHOICES)
    class meta:
        model = TimeEntry





















