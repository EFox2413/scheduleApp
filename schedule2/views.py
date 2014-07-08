from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError

from models import Employee, Area, Availability

from datetime import time

#returns math subject areas
math_list = [x[1] for x in Area.MATH_SUBJECTS]
#returns science subject areas
science_list = [x[1] for x in Area.SCIENCE_SUBJECTS]
#returns business subject areas
business_list = [x[1] for x in Area.BUSINESS_SUBJECTS]
#returns technology subject areas
tech_list = [x[1] for x in Area.TECH_SUBJECTS]

#subject list, returns subjects based on area input
subject_list = []

#for /schedules/
def index(request):
    #returns list of general subject areas
    area_list = ("Math", "Science", "Business", "Technology")
    #returns available semester choices
    semester_list = [x[1] for x in Employee.SEMESTER_CHOICES]
    #returns list of subareas
    subarea_list = [x[1] for x in Area.SUBAREA_CHOICES]
    #day_list return list of day names without abbreviations
    day_list = [x[1] for x in Availability.DAY_CHOICES]
    #time_list returns the available time choices, hardcoded into models.py
    time_list = [x[1] for x in Availability.TIME_CHOICES]

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
    day_list = [day[1] for day in Availability.DAY_CHOICES]
    #time_list returns the available time choices, hardcoded into models.py
    time_list = [time[1] for time in Availability.TIME_CHOICES]

    context = {
                'day_list': day_list,
                'time_list': time_list,
              }

    return render(request, 'schedules/overview.html', context)

def overviewGetData(request):
    if request.method == 'GET':
        message = []

        for employee in Employee.objects.all():
            name = employee.name
            areas = ""
            
            for subarea in employee.area_set.all():
                for subject in Area.MATH_SUBJECTS:
                    if subarea.subarea == subject[0]:
                        areas += "M"
                for subject in Area.SCIENCE_SUBJECTS:
                    if subarea.subarea == subject[0]:
                        areas += "S"
                for subject in Area.BUSINESS_SUBJECTS:
                    if subarea.subarea == subject[0]:
                        areas += "B"
                for subject in Area.TECH_SUBJECTS:
                    if subarea.subarea == subject[0]:
                        areas += "T"

            for availability in employee.availability_set.all():
                timeStart = availability.time_start
                timeEnd = availability.time_end
                dayName = ""

                for day in Availability.DAY_CHOICES:
                    if availability.day == day[0]:
                        dayName = day[1]


                message.append(name + ",")
                message.append(dayName + "," + timeStart.strftime("%I:%M %p") + "," + timeEnd.strftime("%I:%M %p") + ",")
                message.append(areas)
                message.append("\n")

    else:
        message = "Request failed"

    return HttpResponse( message )

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
# should probably refactor this to something different than testPost
def testPost(request):
    print request
    if request.method == 'POST':
        reqName = request.POST['name']
        reqSubAreas = request.POST.getlist('subArea[]')
        reqSemester = request.POST['semester']
        reqAvailability = request.POST.getlist('availability[]')

        for x in Employee.SEMESTER_CHOICES:
            if reqSemester == x[1]:
                empObj = Employee(name=reqName, semester=x[0])

        empObj.save()

        for area in reqSubAreas:
            for x in Area.SUBAREA_CHOICES:
                if area == x[1]:
                    empObj.area_set.create(subarea=x[0])


        for availability in reqAvailability:
            timeArray = availability.split(" ")
            dayInput = timeArray[0]
            timeStartInput = timeArray[1] + " " + timeArray[2]
            timeEndInput = timeArray[3] + " " + timeArray[4]

            for day in Availability.DAY_CHOICES:
                if dayInput == day[1]:
                    reqDay = day[0]

            for time in Availability.TIME_CHOICES:
                if timeStartInput == time[1]:
                    reqTimeStart = time[0]
                if timeEndInput == time[1]:
                    reqTimeEnd = time[0]

            empObj.availability_set.create(day=reqDay, time_start=reqTimeStart, time_end=reqTimeEnd)

    return HttpResponse("name: " + reqName + 
                        "\nsubAreas: " + reqSubAreas[0] +
                        "\nsemester: " + reqSemester +
                        "\navailability: \n" + reqAvailability[0])
