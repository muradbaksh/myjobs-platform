from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from companies.models import Company
from .models import CompanyReview
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_review(request, id):
    company = get_object_or_404(Company, id=id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.company = company

            already = CompanyReview.objects.filter(
                user=request.user,
                company=company
            ).exists()

            if already:
                messages.warning(request,"You already reviewed this company.")
                return redirect('company_detail', id=company.id)
            
            review.save()
            messages.success(request,"Review submitted successfully.")
            return redirect('company_detail', id=company.id)
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'company': company})