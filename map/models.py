from django.db import models

class Course(models.Model):
    courseCode = models.CharField(max_length = 7, primary_key=True)
    courseName = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50)
    def __str__(self):
        return self.courseCode

class Module(models.Model):
    modCode = models.CharField(max_length = 7, primary_key=True)
    modName = models.CharField(max_length = 50)
    def __str__(self):
        return self.modCode

class Building(models.Model):
    buildingCode = models.CharField(max_length = 7, primary_key=True)
    buildingName = models.CharField(max_length = 50)

    def __str__(self):
        return "%s" % self.buildingCode

class Room(models.Model):
    roomCode = models.CharField(max_length = 7, primary_key=True)
    roomName = models.CharField(max_length = 7)
    buildingCode = models.ForeignKey(Building)
    lat = models.CharField(max_length = 7)
    lon = models.CharField(max_length = 7)

    def __str__(self):
        return self.roomCode



class Lecturer(models.Model):
    lecCode = models.CharField(max_length = 7, primary_key=True)
    lecFirst_Name = models.CharField(max_length = 100)
    lecLast_Name = models.CharField(max_length = 100)
    lecEmail = models.EmailField();

    def __str__(self):
        return self.lecCode

class Timetable(models.Model):
    courseCode = models.ForeignKey(Course)
    modCode = models.ForeignKey(Module)
    roomCode = models.ForeignKey(Room)
    lecCode = models.ForeignKey(Lecturer)
    day = models.CharField(max_length = 7)
    time = models.CharField(max_length = 7)

    class Meta:
        unique_together = (("courseCode", "modCode", "day", "time"),)
