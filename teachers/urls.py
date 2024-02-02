from django.urls import path
from . import views

urlpatterns = [
    path('teacher_subjects/', views.teacher_subjects_view, name='teacher_subjects'),
    path('gradebook/<int:classroom>/<str:letter>/<str:subject_name>', views.gradebook_view, name='gradebook'),
    path('create_assigment/', views.gradebook_view, name='create_assigment'),
    path('contact_parent/<int:student>/', views.contact_parent_view, name='contact_parent'),
    path('messages/', views.messages_view, name='messages_view')
]