from multiprocessing.resource_tracker import register

from django.contrib import admin

from exam.models import Course, Lecture

admin.site.register(Course)
admin.site.register(Lecture)
# Register your models here.
