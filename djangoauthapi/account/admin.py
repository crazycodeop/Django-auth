from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):

    # fields to be displayed in admin panel
    list_display = ['id', "email", "name", 'tnc', "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", 'tnc']}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    # when creating user from admin panel
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", 'tnc', "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", 'id']
    filter_horizontal = []

# Registering the new user model admin
admin.site.register(User, UserModelAdmin)
