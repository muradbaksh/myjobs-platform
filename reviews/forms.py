from django import forms
from .models import CompanyReview

RATING_FIELDS = [
    'brand_value', 'work_environment', 'career_growth',
    'salary_satisfaction', 'job_security', 'employee_respect',
    'fringe_benefits', 'leadership_quality', 'work_life_balance',
    'learning_opportunity',
]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = CompanyReview
        exclude = ['user', 'company', 'is_approved', 'is_flagged']
        widgets = {
            field: forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'rating-input'})
            for field in RATING_FIELDS
        }

    def clean(self):
        cleaned_data = super().clean()
        for field in RATING_FIELDS:
            value = cleaned_data.get(field)
            if value is not None and not (1 <= value <= 5):
                self.add_error(field, "Please enter a value between 1 and 5.")
        return cleaned_data