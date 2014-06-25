from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError

from models import Employee, Availability

from datetime import time

#returns math subject areas
math_list = [x[1] for x in Employee.MATH_SUBJECTS]
#returns science subject areas
science_list = [x[1] for x in Employee.SCIENCE_SUBJECTS]
#returns business subject areas
business_list = [x[1] for x in Employee.BUSINESS_SUBJECTS]
#returns technology subject areas
tech_list = [x[1] for x in Employee.TECH_SUBJECTS]

#subject list, returns subjects based on area input
subject_list = []

#for /schedules/
def index(request):
    #returns list of general subject areas
    area_list = [x[1] for x in Employee.AREA_CHOICES]
    #returns list of subareas
    subarea_list = [x[1] for x in Employee.SUBAREA_CHOICES]
    #day_list return list of day names without abbreviations
    day_list = [x[1] for x in Availability.DAY_CHOICES]
    #time_list returns the available time choices, hardcoded into models.py
    time_list = Availability.TIME_CHOICES
    #returns available semester choices
    semester_list = [x[1] for x in Availability.SEMESTER_CHOICES]

    context = { 
                'area_list': area_list,
                'day_list': day_list,
                'time_list': time_list,
                'subarea_list': subarea_list,
                'semester_list': semester_list,
              }
    
    return render(request, 'schedules/index.html', context)

# saves POST'ed data to the database
def submit(request):

    return #HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

#for /schedules/overview
def overview(request):
    #day_list return list of day names without abbreviations
    day_list = [x[1] for x in Availability.DAY_CHOICES]
    #time_list returns the available time choices, hardcoded into models.py
    time_list = Availability.TIME_CHOICES

    context = {
                'day_list': day_list,
                'time_list': time_list,
              }
    return render(request, 'schedules/overview.html', context)

#updates subarea list based on areas list, AJAX
def makeSubList(request):
    print request
    if request.method == 'POST':
        subAreas = request.POST['subAreas']

        if subAreas == '1':
            subject_list = math_list
        if subAreas == '2':
            subject_list = subject_list + math_list
        if subAreas == '3':
            subject_list = subject_list + math_list
        if subAreas == '4':
            subject_list = subject_list + math_list

    return HttpResponse("subAreas: " + subAreas)

# AJAX for seeing if data is correctly submitted
def testPost(request):
    print request
    if request.method == 'POST':
        name = request.POST['name']
        areas = request.POST['areas']
        subAreas = request.POST['subAreas']
        semester = request.POST['semester']
        availability = request.POST['availability']

    return HttpResponse("name: " + name + 
                        "\nareas: " + areas +
                        "\nsubAreas: " + subAreas +
                        "\nsemester: " + semester +
                        "\navailability: " + availability)
