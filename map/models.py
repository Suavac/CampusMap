from django.db import models

class Department(models.Model):
    depName = models.CharField(max_length = 70, primary_key=True)

    def __str__(self):
        return "%s" % self.depName

class Course(models.Model):
    courseCode = models.CharField(max_length = 7, primary_key=True)
    courseName = models.CharField(max_length = 50)
    department = models.ForeignKey(Department)
    def __str__(self):
        return self.courseCode

class Module(models.Model):
    modCode = models.CharField(max_length = 7, primary_key=True)
    modName = models.CharField(max_length = 70)
    def __str__(self):
        return self.modCode

class Building(models.Model):

    buildingName = models.CharField(max_length = 75, primary_key=True)

    def __str__(self):
        return "%s" % self.buildingName


class Room(models.Model):
    roomCode = models.CharField(max_length = 15, primary_key=True) # changed to 15
    roomName = models.CharField(max_length = 30)
    building = models.ForeignKey(Building)
    lat = models.FloatField(max_length = 9)
    lon = models.FloatField(max_length = 9)

    def __str__(self):
        return self.roomCode



class Lecturer(models.Model):
    lecCode = models.CharField(max_length = 7, primary_key=True)
    lecFirst_Name = models.CharField(max_length = 50)
    lecLast_Name = models.CharField(max_length = 50)
    lecEmail = models.EmailField();

    def __str__(self):
        return self.lecCode



class Timetable(models.Model):

    DAY_CHOICES = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    )
    HOURS_CHOICES = (

    )

    courseCode = models.ForeignKey(Course)
    year = models.CharField(max_length = 1)
    semester = models.CharField(max_length = 1)
    modCode = models.ForeignKey(Module)
    roomCode = models.ForeignKey(Room)
    lecCode = models.ForeignKey(Lecturer)
    day = models.CharField(max_length = 1, choices=DAY_CHOICES)
    time = models.CharField(max_length = 7)

    class Meta:
        unique_together = (("year", "semester", "courseCode", "modCode", "day", "time"),)
