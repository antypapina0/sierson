from django.contrib import admin
from .models import Lesson, LessonInstance

# Register your models here.
admin.site.register(Lesson)
admin.site.register(LessonInstance)