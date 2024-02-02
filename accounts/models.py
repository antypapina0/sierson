from django.db import models
from django.contrib.auth.models import AbstractUser

# signals
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE = (("Admin", "Admin"), ("Staff", "Staff"), ("Teacher", "Teacher"), ("Student", "Student"), ("Parent", "Parent"))
    GENDER = [("M", "Male"), ("F", "Female")]

    user_type = models.CharField(default="Admin", choices=USER_TYPE, max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher_subject = models.CharField(max_length=1, blank=True, null=True)
    accounts_customuser = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.last_name + ", " + self.first_name
    
class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.last_name + ", " + self.admin.first_name


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "Admin":
            Admin.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == "Admin":
        instance.admin.save()