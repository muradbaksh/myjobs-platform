from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from .forms import CompanyForm
from reviews.models import CompanyReview
from compensation.models import Compensation
from reviews.utils import calculate_score
from django.db.models import Avg
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def company_list(request):
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
        'top_companies': top_companies,
        'industry_salaries': industry_salaries,
        'recent_reviews': recent_reviews,
    })



def company_detail(request, id):
    company = get_object_or_404(Company, id=id)

    reviews = CompanyReview.objects.filter(company=company, is_approved=True)
    salaries = Compensation.objects.filter(company=company)

    score = calculate_score(company)
    avg_salary = salaries.aggregate(Avg('base_salary'))['base_salary__avg']

    return render(request, 'detail.html', {
        'company': company,
        'reviews': reviews,
        'salaries': salaries,
        'score': score,
        'avg_salary': avg_salary,
    })



@login_required
def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Company added successfully.")
            return redirect('home')
    else:
        form = CompanyForm()
    return render(request,'add_company.html',{'form': form})