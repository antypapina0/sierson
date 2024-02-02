from django.db import models

from teachers.models import Teacher
from subjects.models import Subject

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100, unique=False)
    post_code = models.CharField(max_length=10, unique=False)
    address = models.TextField(max_length=200, unique=False)

    def __str__(self):
        return self.name
    
# class Term(models.Model):
#     TERM_CHOICES = [
#         ('1', 'semestr 1'),
#         ('2', 'semestr 2')
#     ]

#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     term_name = models.CharField(max_length=15, choices=TERM_CHOICES)
#     start_date = models.DateField()
#     end_date = models.DateField()

#     def __str__(self):
#         return f"{self.term_name} - {self.school}"

# class SubjectTerm(models.Model):
#     term = models.ForeignKey(Term, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.term} {self.subject}"
    
class Term(models.Model):
    term_year_start = models.IntegerField()
    term_year_end = models.IntegerField()

    term_start_sem_1 = models.DateField()
    term_end_sem_1 = models.DateField()

    term_start_sem_2 = models.DateField()
    term_end_sem_2 = models.DateField()
    
    def __str__(self):
        return f"{self.term_year_start}/{self.term_year_end} | semestr 1: {self.term_start_sem_1} - {self.term_end_sem_1} | semestr 2: {self.term_start_sem_2} - {self.term_end_sem_2}"

class Class(models.Model):
    CLASS_CHOICES = [
        ('1', 'Klasa 1'),
        ('2', 'Klasa 2'),
        ('3', 'Klasa 3'),
        ('4', 'Klasa 4'),
        ('5', 'Klasa 5')
    ]

    CLASS_LETTER_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    ]

    class_name = models.CharField(max_length=10, choices=CLASS_CHOICES)
    class_letter = models.CharField(max_length=1, choices=CLASS_LETTER_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # counselor = models.ForeignKey(Teacher, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.class_name} {self.class_letter} - {self.school}"

class Classroom(models.Model):
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.room_number}"


