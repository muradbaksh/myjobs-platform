

# def calculate_score(company):
#     from .models import CompanyReview
#     reviews = CompanyReview.objects.filter(company=company)

#     if not reviews.exists():
#         return 0

#     total = 0
#     count = reviews.count()

#     for r in reviews:
#         total += (
#             r.brand_value +
#             r.work_environment +
#             r.career_growth +
#             r.salary_satisfaction +
#             r.job_security +
#             r.employee_respect +
#             r.fringe_benefits +
#             r.leadership_quality +
#             r.work_life_balance +
#             r.learning_opportunity
#         )

#     return round(total / (count * 50) * 100, 2)


from django.db.models import Avg
from .models import CompanyReview

def calculate_score(company):
    reviews = CompanyReview.objects.filter(company=company)

    if not reviews.exists():
        return 0

    fields = [
        'brand_value', 'work_environment', 'career_growth',
        'salary_satisfaction', 'job_security', 'employee_respect',
        'fringe_benefits', 'leadership_quality', 'work_life_balance',
        'learning_opportunity',
    ]

    total_score = 0

    for field in fields:
        avg = reviews.aggregate(avg=Avg(field))['avg'] or 0
        total_score += avg

    # max possible = 10 fields * 5 = 50
    score = (total_score / 50) * 100

    # safety clamp (important)
    return round(min(max(score, 0), 100), 2)