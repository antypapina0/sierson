from django.db import models

from accounts.models import CustomUser

# signals
from django.dispatch import receiver
from django.db.models.signals import post_save

class Staff(models.Model):
    staff = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff.last_name + " " + self.staff.first_name

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "Staff":
            Staff.objects.create(staff=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == "Staff":
        instance.staff.save()