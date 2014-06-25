from django.db import models

from datetime import time


class Employee(models.Model):
    AREA_CHOICES = (
            ('M', 'Math'),
            ('S', 'Science'),
            ('B', 'Business'),
            ('T', 'Technology'),
            )

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

    emp_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    area = models.CharField(max_length = 1,
                            choices = AREA_CHOICES,
                            default = AREA_CHOICES[0])
    subarea = models.CharField(max_length = 12,
                               choices = SUBAREA_CHOICES,
                               default = SUBAREA_CHOICES[0])
    
    def __unicode__(self):
        return self.name

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
        time_stack = []

        for i in range(7, 20):
            for x in range(0, 2):
                if x == 0 and not i == 7:
                    time_stack.append(time(i).strftime("%I:%M %p"))
                elif x == 1:
                    time_stack.append(time(i, 30).strftime("%I:%M %p"))

        return time_stack

    TIME_CHOICES = make_times()
    RTIME_CHOICES = (TIME_CHOICES, TIME_CHOICES)
    SEMESTER_CHOICES = (
            ('FA', 'Fall 2014'),
            ('SP', 'Spring 2014'),
            ('SU', 'Summer 2014'),
            )

    employee = models.ForeignKey(Employee)
    day = models.CharField(max_length = 1,
                           choices = DAY_CHOICES,
                           default = DAY_CHOICES[0][0])
    time_start = models.CharField(max_length = 50)
    semester = models.CharField(max_length = 2,
                           choices = SEMESTER_CHOICES,
                           default = SEMESTER_CHOICES[0])

    def __unicode__(self):
        return self.format_day_time(self.day, self.time_start)
