from django import forms

from .models import Course, Module, Lecturer, Room, Building

class CourseForm(forms.ModelForm):

    courseCode = forms.CharField(max_length=7)
    courseName = forms.CharField(max_length=7)
    department = forms.CharField(max_length=7)

    class Meta:
        model = Course

class ModuleForm(forms.ModelForm):

    modCode = forms.CharField(max_length=7)
    modName = forms.CharField(max_length=7)

    class Meta:
        model = Module

class RoomForm(forms.ModelForm):

    modCode = forms.CharField(max_length=7)
    modName = forms.CharField(max_length=7)
    roomCode = forms.CharField(max_length = 7)
    roomName = forms.CharField(max_length = 7)
    building = forms.CharField(max_length = 7)
    lat = forms.CharField(max_length = 7)
    lon = forms.CharField(max_length = 7)

    class Meta:
        model = Room

class BuildingForm(forms.ModelForm):

    buildingCode = forms.CharField(max_length = 7)
    buildingName = forms.CharField(max_length = 50)

    class Meta:
        model = Building

class LecturerForm(forms.ModelForm):

    lecCode = forms.CharField(max_length = 7)
    lecFirst_Name = forms.CharField(max_length = 100)
    lecLast_Name = forms.CharField(max_length = 100)
    lecEmail = forms.EmailField();
    class Meta:
        model = Lecturer

