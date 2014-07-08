from django.db import models

from datetime import time


class Employee(models.Model):
    SEMESTER_CHOICES = (
            ('FA', 'Fall 2014'),
            ('SP', 'Spring 2014'),
            ('SU', 'Summer 2014'),
            )

    
    name = models.CharField(max_length=50)
    semester = models.CharField(max_length = 2,
                           choices = SEMESTER_CHOICES,
                           default = SEMESTER_CHOICES[0])
    
    def __unicode__(self):
        return self.name + " " + self.semester

class Area(models.Model):
    MATH_SUBJECTS = (
            ('LIB', 'Liberal Arts Math'),
            ('ALG', 'College Algebra'),
            )

    SCIENCE_SUBJECTS = (
            ('CHM', 'General Chemistry'),
            ('PHY', 'College Physics'),
            )

    BUSINESS_SUBJECTS = (
            ('ECO', 'Economics'),
            ('ACC', 'Accounting'),
            )

    TECH_SUBJECTS = (
            ('TEC', 'Technical Support'),
            ('PRG', 'Computer Programming'),
            )

    SUBAREA_CHOICES = (MATH_SUBJECTS + SCIENCE_SUBJECTS + BUSINESS_SUBJECTS +
                       TECH_SUBJECTS)

    employee = models.ForeignKey(Employee)
    subarea = models.CharField(max_length = 3,
                            choices = SUBAREA_CHOICES,
                            default = SUBAREA_CHOICES[0])

    def __unicode__(self):
        return self.subarea


class Availability(models.Model):
    DAY_CHOICES = (
            ('M', 'Monday'),
            ('T', 'Tuesday'),
            ('W', 'Wednesday'),
            ('R', 'Thursday'),
            ('F', 'Friday'),
            ('S', 'Saturday'),
            ('U', 'Sunday'),
            )

    #makes a list of times in half hour increments ranging from 0:00 to 24:00
    def make_times():
        time_tuple = ()

        for i in range(7, 20):
            for x in range(0, 2):
                if x == 0 and not i == 7:
                    time_tuple += ((time(i), time(i).strftime("%I:%M %p")),)
                elif x == 1:
                    time_tuple += ((time(i, 30), time(i, 30).strftime("%I:%M %p")),)
        return time_tuple

    TIME_CHOICES = make_times()
        
    employee = models.ForeignKey(Employee)
    day = models.CharField(max_length = 1,
                           choices = DAY_CHOICES,
                           default = DAY_CHOICES[0][0])
    time_start = models.TimeField(choices = TIME_CHOICES)
    time_end = models.TimeField(choices = TIME_CHOICES)

    def __unicode__(self):
        returnString = ("Day: " + self.day + " Beg: " + self.time_start.strftime("%I:%M %p") + 
                     " End: " + self.time_end.strftime("%I:%M %p"))

        return returnString
