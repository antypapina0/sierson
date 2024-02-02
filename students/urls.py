from django.urls import path
from . import views

urlpatterns = [
    path('grades/', views.student_grades_view, name='student_grades'),
]