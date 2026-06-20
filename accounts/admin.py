from django.contrib import admin
from .models import User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'email',
        'credits',
        'is_verified',
        'is_staff'
    )

    list_filter = (
        'is_verified',
        'is_staff'
    )

    search_fields = (
        'username',
        'email'
    )

    list_editable = (
        'credits',
        'is_verified'
    )