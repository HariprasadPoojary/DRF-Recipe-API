from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

# Register your models here.
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = [
        "email",
        "name",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": ("email", "password"),
            },
        ),
        (
            _("Personal Info"),
            {
                "fields": ("name",),
            },
        ),
        (
            _("Permisssions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": ("last_login",),
            },
        ),
    )


admin.site.register(User, UserAdmin)
