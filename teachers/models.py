from django.db import models

from accounts.models import CustomUser
from subjects.models import Subject

# signals
from django.dispatch import receiver
from django.db.models.signals import post_save

class Teacher(models.Model):
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.teacher.last_name + " " + self.teacher.first_name

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "Teacher":
            Teacher.objects.create(teacher=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == "Teacher":
        instance.teacher.save()