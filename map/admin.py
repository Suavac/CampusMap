from django.contrib import admin

# Register your models here.
from .models import Course, Module, Lecturer, Building, Timetable, Department, TimeEntry, Room, Colour

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('courseCode', 'year', 'semester')
    list_filter = ('courseCode','year',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseCode', 'courseName', 'department')
    list_filter = ('courseCode',)


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('modCode', 'modName', 'color')
    list_filter = ('modCode',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('roomName', 'roomCode', 'building')
    list_filter = ('building',)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('lecFirst_Name', 'lecLast_Name', 'lecCode')
    list_filter = ('lecFirst_Name', 'lecLast_Name',)

class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ('modCode', 'roomCode', 'day', 'time', 'lecCode')
    list_filter = ('day', 'modCode', 'roomCode',)

class ColourAdmin(admin.ModelAdmin):
    list_display = ('colour', 'hex')

admin.site.register(TimeEntry, TimeEntryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Building)
admin.site.register(Room, RoomAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Department)
admin.site.register(Lecturer, LecturerAdmin)