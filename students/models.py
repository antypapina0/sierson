from django.db import models

from accounts.models import CustomUser
from school.models import Class
from parents.models import Parent

# signals
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

class Student(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.SET_NULL, related_name='students', null=True)

    def __str__(self):
        return self.student.last_name + " " + self.student.first_name

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "Student":
            Student.objects.create(student=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == "Student":
        instance.student.save()

@receiver(post_delete, sender=Student)
def delete_user(sender, instance, **kwargs):
    if instance.student:
        instance.student.delete()