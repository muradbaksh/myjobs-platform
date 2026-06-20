from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User
from companies.models import Company

RATING_VALIDATORS = [MinValueValidator(1), MaxValueValidator(5)]

class CompanyReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    brand_value = models.IntegerField(validators=RATING_VALIDATORS)
    work_environment = models.IntegerField(validators=RATING_VALIDATORS)
    career_growth = models.IntegerField(validators=RATING_VALIDATORS)
    salary_satisfaction = models.IntegerField(validators=RATING_VALIDATORS)
    job_security = models.IntegerField(validators=RATING_VALIDATORS)

    employee_respect = models.IntegerField(default=0, validators=RATING_VALIDATORS)
    fringe_benefits = models.IntegerField(default=0, validators=RATING_VALIDATORS)
    leadership_quality = models.IntegerField(default=0, validators=RATING_VALIDATORS)
    work_life_balance = models.IntegerField(default=0, validators=RATING_VALIDATORS)
    learning_opportunity = models.IntegerField(default=0, validators=RATING_VALIDATORS)

    recommendation = models.BooleanField(default=True)
    anonymous = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_approved = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.user.credits += 10
            self.user.save()