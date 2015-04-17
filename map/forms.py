from django import forms
from django.template.defaultfilters import mark_safe

from .models import Course, Module, Lecturer, Room, Building, Timetable, Department, TimeEntry, Colour

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
    colour = Colour.objects.all()

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

class TimeEntryForm(forms.ModelForm):

    DAY_CHOICES = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
    )

    HOURS_CHOICES = (
        ('1', '09:00'),
        ('2', '10:00'),
        ('3', '11:00'),
        ('4', '12:00'),
        ('5', '13:00'),
        ('6', '14:00'),
        ('7', '15:00'),
        ('8', '16:00'),
        ('9', '17:00'),
        ('10', '18:00'),
        ('11', '19:00'),
    )

    timeTable = Timetable.objects.all()
    modCode = Module.objects.all()
    roomCode = Room.objects.all()
    lecCode = Lecturer.objects.all()
    day = forms.ChoiceField(choices=DAY_CHOICES)
    time = forms.ChoiceField(choices=HOURS_CHOICES)

    class Meta:
        model = TimeEntry
        fields = "__all__"