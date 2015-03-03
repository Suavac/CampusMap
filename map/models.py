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
    roomName = models.CharField(max_length = 30)                    # Change 7 to 30
    buildingCode = models.ForeignKey(Building)
    lat = models.FloatField(max_length = 9)                         # Char to Float and size 7 to 9
    lon = models.FloatField(max_length = 9)

    def __str__(self):
        return self.roomCode



class Lecturer(models.Model):
    lecCode = models.CharField(max_length = 7, primary_key=True)
    lecFirst_Name = models.CharField(max_length = 50)               # Reduced size from 100 to 50
    lecLast_Name = models.CharField(max_length = 50)
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
