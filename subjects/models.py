from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name

