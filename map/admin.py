from django.contrib import admin

# Register your models here.
from .models import Course, Module, Lecturer, Building, Timetable, Department, Time, Room

class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseCode', 'courseName', 'department')
    list_filter = ('courseCode',)


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('modCode', 'modName')
    list_filter = ('modCode',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('roomName', 'roomCode', 'building')
    list_filter = ('roomName',)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('lecFirst_Name', 'lecLast_Name', 'lecCode')
    list_filter = ('lecFirst_Name', 'lecLast_Name',)


class TimeAdmin(admin.ModelAdmin):
    list_display = ('modCode', 'roomCode', 'day', 'time')
    list_filter = ('day', 'roomCode',)


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('courseCode', 'year', 'semester')
    list_filter = ('year',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Building)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Room)
admin.site.register(Department)
admin.site.register(Lecturer, LecturerAdmin)