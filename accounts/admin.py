from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Admin
from django.contrib.auth.models import User

from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'user_type', 'gender', 'address')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "first_name", "last_name", 'user_type', "password1", "password2"),
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Admin)
