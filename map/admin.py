from django.contrib import admin

# Register your models here.
from .models import Course, Module, Lecturer, Building, Timetable, Department

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Building)
admin.site.register(Timetable)
admin.site.register(Department)
admin.site.register(Lecturer)