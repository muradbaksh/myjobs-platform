from django.contrib import admin
from .models import CompanyReview

@admin.register(CompanyReview)
class CompanyReviewAdmin(admin.ModelAdmin):

    list_display = (
        'company',
        'user',
        'created_at',
        'is_approved',
        'is_flagged'
    )

    list_filter = (
        'is_approved',
        'is_flagged',
        'created_at'
    )

    search_fields = (
        'company__name',
        'user__username',
        'user__email'
    )

    actions = [
        'approve_reviews',
        'flag_reviews'
    ]

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)

    def flag_reviews(self, request, queryset):
        queryset.update(is_flagged=True)