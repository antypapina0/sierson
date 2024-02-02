from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect

from grades.models import Grade
from .models import Student
from schedule.models import Lesson
from subjects.models import Subject

def student_grades_view(request):

    grades = Grade.objects.filter(student=request.user.student)
    student = Student.objects.get(id=request.user.student.id)
    lessons = Lesson.objects.filter(class_id = student.class_id)
    dist_lessons = Lesson.objects.filter(class_id = student.class_id).values(
        'class_id',
        'class_id__class_name',
        'class_id__class_letter',
        'class_id__school',
        'teacher_id',
        'subject_id__subject_name',
        'subject_id__id',
        'class_id__id').distinct()

    student_grades = {}
    for lesson in dist_lessons:
        subject = Subject.objects.get(subject_name=lesson['subject_id__subject_name'])
        student_grades[subject.subject_name] = Grade.get_all_student_subject_grades(student, subject)

    context = {
        'student_grades': student_grades
        }

    return render(request, 'students/student_grades.html', context=context)