from django.db import models

from accounts.models import CustomUser

# signals
from django.dispatch import receiver
from django.db.models.signals import post_save

class Parent(models.Model):
    parent = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.parent.last_name + " " + self.parent.first_name

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "Parent":
            Parent.objects.create(parent=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == "Parent":
        instance.parent.save()
