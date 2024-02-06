from django.contrib import admin

from .models import Student, StudentAttendance

admin.site.register(Student)
admin.site.register(StudentAttendance)