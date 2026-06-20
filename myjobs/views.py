from django.shortcuts import render, redirect, get_object_or_404
from companies.models import Company
from reviews.models import CompanyReview
from compensation.models import Compensation
from reviews.utils import calculate_score
from django.db.models import Avg
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# def company_list(request):
#     q = request.GET.get('q')
#     companies = Company.objects.all()
    
#     if q:
#         companies = companies.filter(
#             Q(name__icontains=q) |
#             Q(industry__icontains=q) |
#             Q(location__icontains=q) |
#             Q(size__icontains=q)
#         )
#         # Top rated companies (verified, score > 0)
#     all_verified = Company.objects.filter(is_verified=True)
#     top_companies = sorted(
#         all_verified,
#         key=lambda c: c.reputation_score(),
#         reverse=True
#     )[:3]

#     # Industry salary insights
#     from compensation.models import Compensation
#     from reviews.models import CompanyReview

#     industry_salaries = Compensation.objects.values(
#         'company__industry'
#     ).annotate(avg_salary=Avg('base_salary')).order_by('-avg_salary')[:5]

#     # Recent approved reviews
#     recent_reviews = CompanyReview.objects.filter(
#         is_approved=True
#     ).select_related('company').order_by('-created_at')[:4]


#     return render(request, 'home.html', {
#         'companies': companies,
#         'top_companies': top_companies,
#         'industry_salaries': industry_salaries,
#         'recent_reviews': recent_reviews,
#     })




def home(request):
    companies = Company.objects.all()
    # context = {
    #     "companies": companies,
    #     "company_count": Company.objects.count(),
    #     "review_count": Review.objects.count(),
    #     "salary_count": SalaryReport.objects.count(),
    # }

    q = request.GET.get('q')
    companies = Company.objects.all()
    
    if q:
        companies = companies.filter(
            Q(name__icontains=q) |
            Q(industry__icontains=q) |
            Q(location__icontains=q) |
            Q(size__icontains=q)
        )
        # Top rated companies (verified, score > 0)
    all_verified = Company.objects.filter(is_verified=True)
    top_companies = sorted(
        all_verified,
        key=lambda c: c.reputation_score(),
        reverse=True
    )[:3]

    # Industry salary insights
    from compensation.models import Compensation
    from reviews.models import CompanyReview

    industry_salaries = Compensation.objects.values(
        'company__industry'
    ).annotate(avg_salary=Avg('base_salary')).order_by('-avg_salary')[:5]

    # Recent approved reviews
    recent_reviews = CompanyReview.objects.filter(
        is_approved=True
    ).select_related('company').order_by('-created_at')[:4]


    return render(request, 'home.html', {
        'companies': companies,
        'company_count': Company.objects.count(),
        'review_count': CompanyReview.objects.count(),
        'salary_count': Compensation.objects.count(),
        'top_companies': top_companies,
        'industry_salaries': industry_salaries,
        'recent_reviews': recent_reviews,
    })
