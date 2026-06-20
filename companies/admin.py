from django.contrib import admin
from .models import Company


# admin.site.register(Company)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'industry',
        'location',
        'is_verified'
    )

    list_filter = (
        'industry',
        'is_verified'
    )

    search_fields = (
        'name',
        'industry'
    )

    list_editable = (
        'is_verified',
    )

    actions = [
        'verify_company'
    ]

    def verify_company(self, request, queryset):
        queryset.update(is_verified=True)

    verify_company.short_description = "Verify selected companies"
