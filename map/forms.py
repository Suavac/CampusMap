from django import forms
from django.template.defaultfilters import mark_safe

from .models import Course, Module, Lecturer, Room, Building, Timetable, Department, TimeEntry

class DepartmentForm(forms.ModelForm):

    depName = forms.CharField(max_length = 50,label = mark_safe('<strong>Department Name</strong>'))

    class Meta:
        model = Department
        fields = "__all__"

class CourseForm(forms.ModelForm):

    courseCode = forms.CharField(max_length=15,label = mark_safe('<strong>Code</strong>'))
    courseName = forms.CharField(max_length=50,label = mark_safe('<strong>Name</strong>'))
    department = queryset=Department.objects.all()

    class Meta:
        model = Course
        fields = "__all__"

class ModuleForm(forms.ModelForm):

    modCode = forms.CharField(max_length=7, label = mark_safe('<strong>Module Code</strong>'))
    modName = forms.CharField(max_length=70,label = mark_safe('<strong>Module Name</strong>'))

    class Meta:
        model = Module
        fields = "__all__"

class BuildingForm(forms.ModelForm):

    buildingName = forms.CharField(max_length = 75,label = mark_safe('<strong>Building Name</strong>'))

    class Meta:
        model = Building
        fields = "__all__"

class RoomForm(forms.ModelForm):

    roomCode = forms.CharField(max_length = 15,label = mark_safe('<strong>Room Code</strong>'))
    roomName = forms.CharField(max_length = 30,label = mark_safe('<strong>Room Name</strong>'))
    building = queryset=Building.objects.all()
    #lat = forms.CharField(max_length = 19, label = mark_safe('<strong>Latitude</strong>'))
    #lng = forms.CharField(max_length = 19, label = mark_safe('<strong>Longitude</strong>'))

    class Meta:
        model = Room
        fields = "__all__"

class LecturerForm(forms.ModelForm):

    lecCode = forms.CharField(max_length = 7,label = mark_safe('<strong>Code</strong>'),)
    lecFirst_Name = forms.CharField(max_length = 50,label = mark_safe('<strong>First Name</strong>'))
    lecLast_Name = forms.CharField(max_length = 50,label = mark_safe('<strong>Last Name</strong>'))
    lecEmail = forms.EmailField(label = mark_safe('<strong>Email</strong>'))
    class Meta:
        model = Lecturer
        fields = "__all__"

class TimetableForm(forms.ModelForm):

    courseCode = Course.objects.all()
    year = forms.CharField(max_length = 1)
    semester = forms.CharField(max_length = 1)
    class Meta:
        model = Timetable
        fields = "__all__"

class TimeEntry(forms.ModelForm):

    timeTable = Timetable.objects.all()
    modCode = Module.objects.all()
    roomCode = Room.objects.all()
    lecCode = Lecturer.objects.all()
    day = forms.CharField(max_length = 1)
    time = forms.CharField(max_length = 2)

    class meta:
        model = TimeEntry
        fields = "__all__"