from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def average_salary(self):
        salaries = self.compensation_set.all()

        if salaries.exists():
            return sum(
                s.base_salary for s in salaries
            ) / salaries.count()
        return 0

    def reputation_score(self):
        from reviews.utils import calculate_score  
        return calculate_score(self)
    
    def total_reviews(self):
        return self.companyreview_set.count()
        
    def __str__(self):
        return self.name