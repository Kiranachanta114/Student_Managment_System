from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'email', 'course']

admin.site.register(Student, StudentAdmin)


# Register your models here.
