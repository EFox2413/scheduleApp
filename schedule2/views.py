from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from models import Employee, Availability

from datetime import time

def index(request):
    #returns list of general subject areas
    area_list = [x[1] for x in Employee.AREA_CHOICES]
    #returns list of subareas
    subarea_list = [x[1] for x in Employee.SUBAREA_CHOICES]
    #day_list return list of day names without abbreviations
    day_list = [x[1] for x in Availability.DAY_CHOICES]
    #time_list returns the available time choices, hardcoded into models.py
    time_list = Availability.TIME_CHOICES
    context = { 
                'area_list': area_list,
                'day_list': day_list,
                'time_list': time_list,
                'subarea_list': subarea_list,
              }
    return render(request, 'schedules/index.html', context)

def aggregate(request):
    context = {}
    return render(request, 'schedules/timeData', context)
