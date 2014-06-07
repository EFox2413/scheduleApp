from django.db import models

from datetime import time


class Employee(models.Model):
    AREA_CHOICES = (
            ('M', 'Math'),
            ('S', 'Science'),
            ('B', 'Business'),
            ('T', 'Technology'),
            )

    SUBAREA_CHOICES = (
            ('LIB', 'Liberal Arts Math'),
            ('ALG', 'College Algebra'),
            ('CHM', 'General Chemistry'),
            ('PHY', 'College Physics'),
            ('ECO', 'Economics'),
            ('ACC', 'Accounting'),
            ('TEC', 'Technical Support'),
            ('PRG', 'Computer Programming'),
            )


    emp_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    area = models.CharField(max_length = 1,
                               choices = AREA_CHOICES,
                               default = AREA_CHOICES[0][0])
    subarea = models.CharField(max_length = 12,
                               choices = SUBAREA_CHOICES)
    
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
    

    employee = models.ForeignKey(Employee)
    day = models.CharField(max_length = 1,
                           choices = DAY_CHOICES,
                           default = DAY_CHOICES[0][0])
    time_start = models.TimeField('start time of availability')
    time_end = models.TimeField('end time of availability')

    #formats the response of availability in a day and time range object
    def format_day_time(self, input_day, input_start, input_end):
        day = input_day
        start = input_start
        end = input_end

        format_response = "%s: From %s to %s" % (day, start, end)

        return format_response

    def calc_time_delta(self, start, end):
        time_range = end - start
        return str(time_range)

    def __unicode__(self):
        return self.format_day_time(self.day, self.time_start, self.time_end)

    def is_available(self, hour):
        if time_start < hour < time_end:
            return "%s is available." % self.employee 

        return "%s is not available." % self.employee
