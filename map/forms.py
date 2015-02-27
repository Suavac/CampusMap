from django import forms
from django.template.defaultfilters import mark_safe

from .models import Course, Module, Lecturer, Room, Building, Timetable

class CourseForm(forms.ModelForm):

    courseCode = forms.CharField(max_length=7,label = mark_safe('<strong>Code</strong>'))
    courseName = forms.CharField(max_length=50,label = mark_safe('<strong>Name</strong>'))
    department = forms.CharField(max_length=50,label = mark_safe('<strong>Department</strong>'))

    class Meta:
        model = Course

class ModuleForm(forms.ModelForm):

    modCode = forms.CharField(max_length=7, label = mark_safe('<strong>Module Code</strong>'))
    modName = forms.CharField(max_length=50,label = mark_safe('<strong>Module Name</strong>'))

    class Meta:
        model = Module

class RoomForm(forms.ModelForm):

    roomCode = forms.CharField(max_length = 7,label = mark_safe('<strong>Room Code</strong>'))
    roomName = forms.CharField(max_length = 30,label = mark_safe('<strong>Room Name</strong>'))
    buildingCode = queryset=Building.objects.all()
    lat = forms.CharField(max_length = 9, label = mark_safe('<strong>Latitude</strong>'))
    lon = forms.CharField(max_length = 9, label = mark_safe('<strong>Longitude</strong>'))

    class Meta:
        model = Room

class BuildingForm(forms.ModelForm):

    buildingCode = forms.CharField(max_length = 7,label = mark_safe('<strong>Building Code</strong>'))
    buildingNameE = forms.CharField(max_length = 75,label = mark_safe('<strong>Building Name</strong>'))
    buildingNameI = forms.CharField(max_length = 75,label = mark_safe('<strong>Building Name</strong>'))

    class Meta:
        model = Building

class LecturerForm(forms.ModelForm):

    lecCode = forms.CharField(max_length = 7,label = mark_safe('<strong>Code</strong>'),)
    lecFirst_Name = forms.CharField(max_length = 50,label = mark_safe('<strong>First Name</strong>'))
    lecLast_Name = forms.CharField(max_length = 50,label = mark_safe('<strong>Last Name</strong>'))
    lecEmail = forms.EmailField(label = mark_safe('<strong>Email</strong>'))
    class Meta:
        model = Lecturer

class TimetableForm(forms.ModelForm):

    courseCode = Course.objects.all()
    modCode = Module.objects.all()
    roomCode = Room.objects.all()
    lecCode = Lecturer.objects.all()
    day = forms.CharField(max_length = 7)
    time = forms.CharField(max_length = 7)
    class Meta:
        model = Timetable