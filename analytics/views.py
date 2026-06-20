from django.shortcuts import render
from companies.models import Company
from compensation.models import Compensation
from django.db.models import Avg
import json


def analytics_dashboard(request):
    top_companies = Company.objects.filter(is_verified=True)
    company_data = []

    for company in top_companies:
        company_data.append({
            'company': company,
            # 'score': company.average_salary()
            'score': company.reputation_score()
        })

    company_data.sort(
        key=lambda x: x['score'],
        reverse=True
    )
     
    # Chart.js Data
    company_names = []
    company_scores = []

    for item in company_data[:10]:
        company_names.append(
            item['company'].name
        )

        company_scores.append(
            item['score']
        )


    industry_data = Compensation.objects.values(
        'company__industry'
    ).annotate(
        avg_salary=Avg('base_salary')
    )
    return render(request,'dashboard.html',{
        'companies': company_data[:10],
        'data': industry_data,
        # Chart Data
        'labels': json.dumps(company_names),
        'scores': json.dumps(company_scores),
        })


def industry_salary(request):
    data = Compensation.objects.values(
        'company__industry'
    ).annotate(
        avg_salary=Avg('base_salary')
    )

    return render(request,'industry_salary.html',{'data': data})