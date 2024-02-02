# signals
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "Admin":
            Admin.objects.create(admin=instance)
        if instance.user_type == "Staff":
            Staff.objects.create(staff=instance)
        if instance.user_type == "Teacher":
            Teacher.objects.create(teacher=instance)
        if instance.user_type == "Student":
            Student.objects.create(student=instance)
        if instance.user_type == "Parent":
            Parent.objects.create(parent=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == "Admin":
        instance.admin.save()
    if instance.user_type == "Staff":
        instance.staff.save()
    if instance.user_type == "Teacher":
        instance.teacher.save()
    if instance.user_type == "Student":
        instance.student.save()
    if instance.user_type == "Parent":
        instance.parent.save()
