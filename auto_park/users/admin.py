from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import User

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "phone_number", "is_active", "is_staff")
    list_display_links = ("id", "phone_number")
    search_fields = ("id", "phone_number")
    ordering = ("id", "phone_number",)
    readonly_fields = ("date_joined", "last_login")

    fieldsets = [
        (
            "User's data",
            {
                'fields': (
                    "phone_number", "password",
                    "date_joined", "last_login"
                )
            }
        ),
        (
            "Permissions",
            {
                'fields': ("is_staff", "is_active", "is_superuser")
            }
        )
    ]

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password1", "password2"),
            },
        ),
    )