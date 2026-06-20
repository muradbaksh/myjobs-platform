from django.db import models
from accounts.models import User
from companies.models import Company
from django.db.models import Avg


class Compensation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    job_title = models.CharField(max_length=200)
    base_salary = models.IntegerField()
    bonus = models.IntegerField()
    allowance = models.IntegerField()

    market_rating = models.IntegerField()
    anonymous = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.user.credits += 5
            self.user.save()
    
