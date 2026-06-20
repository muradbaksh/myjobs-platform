from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompensationForm
from companies.models import Company
from django.db.models import Avg
from .models import Compensation
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages


@login_required
def add_salary(request, id):
    company = get_object_or_404(Company, id=id)
    if request.method == "POST":
        form = CompensationForm(request.POST)
        if form.is_valid():
            salary = form.save(commit=False)
            salary.user = request.user
            salary.company = company
            salary.save()
            messages.success(request,"Salary information submitted.")
            return redirect('company_detail', id=company.id)
    else:
        form = CompensationForm()

    return render(request, 'add_salary.html', {'form': form,'company': company})




@login_required
def benchmark(request):
    if request.user.credits < 5:
        return HttpResponse(
            "Not enough credits to view benchmark. Need minimum 5 credits."
        )
    request.user.credits -= 5
    request.user.save()

    data = Compensation.objects.values(
        'job_title'
    ).annotate(
        avg_salary=Avg('base_salary')
    )

    return render(
        request,
        'benchmark.html',
        {'data': data}
    )