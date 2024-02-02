from django.db import models
from school.models import Class, School, Classroom, Term
from teachers.models import Teacher
from subjects.models import Subject

from datetime import datetime


class Lesson(models.Model):
    DAY_CHOICES = [
        ('Poniedziałek', 'Poniedziałek'),
        ('Wtorek', 'Wtorek'),
        ('Środa', 'Środa'),
        ('Czwartek', 'Czwartek'),
        ('Piątek', 'Piątek'),
    ]

    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    room_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    term_id = models.ForeignKey(Term, on_delete=models.CASCADE)
    day = models.CharField(max_length=12, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_id} {self.subject_id} {self.day} {self.start_time} - {self.end_time} / {self.term_id}"
    
    @classmethod
    def get_lessons_with_correct_term(cls, id):
        current_date = datetime.now()
        formated_current_date = current_date.strftime("%Y-%m-%d")

        print(formated_current_date)
        return cls.objects.filter(class_id = id)
    
    

