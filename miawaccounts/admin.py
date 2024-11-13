from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Display fields in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'birth_date', 'is_staff', 'is_admin', 'is_pelanggan', 'gender')

    # Add filters in the admin interface
    list_filter = ('is_staff', 'is_admin', 'is_pelanggan', 'gender', 'birth_date')

    # Add search functionality in the admin interface
    search_fields = ('username', 'email', 'first_name', 'last_name', 'birth_date')

    # Define the fieldsets for the user form in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informasi Pribadi', {'fields': ('first_name', 'last_name', 'birth_date', 'gender', 'address', 'phone_number', 'image', 'email')}),
        ('Status', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_pelanggan')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )

    # Define the fields for the "add user" form in the admin interface
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'birth_date', 'password1', 'password2'),
        }),
    )

    # Define the ordering of users
    ordering = ('username',)

# Register the CustomUserAdmin with the User model
admin.site.register(User, CustomUserAdmin)