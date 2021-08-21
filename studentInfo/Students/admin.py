from django.contrib import admin
from .models import Student,StudentAcademics
# Register your models here.

admin.site.register(StudentAcademics)
admin.site.register(Student)
