from django.contrib import admin
from schedule2.models import Employee, Availability

class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,              {'fields': ['name']}), 
            (None,              {'fields': ['emp_id']}),
            ('Knowledge Areas', {'fields': ['area']}),
            ]
    inlines = [AvailabilityInline]

admin.site.register(Employee, EmployeeAdmin)
