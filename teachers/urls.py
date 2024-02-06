from django.urls import path
from . import views

urlpatterns = [
    path('teacher-subjects/', views.teacher_subjects_view, name='teacher_subjects'),
    path('gradebook/<int:classroom>/<str:letter>/<str:subject_name>', views.gradebook_view, name='gradebook'),
    path('create-assigment/', views.gradebook_view, name='create_assigment'),
    path('contact-parent/<int:student>/', views.contact_parent_view, name='contact_parent'),
    path('messages/', views.messages_view, name='messages_view'),
    path('my-class/', views.my_class_view, name='my_class_view'),
    path('lessons/<int:classroom>/<str:letter>/<str:subject_name>', views.lessons_view, name='lessons_view'),
    path('check_attendance/<int:id>/', views.check_attendance_view, name='check_attendance'),
    path('start_lesson/<int:id>/', views.start_lesson, name='start_lesson'),
    path('end_lesson/<int:id>/', views.end_lesson, name='end_lesson'),
]