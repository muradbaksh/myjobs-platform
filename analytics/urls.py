from django.urls import path
from . import views

urlpatterns = [
    path('',views.analytics_dashboard,name='analytics'),
    path('industry-salary/',views.industry_salary,name='industry_salary'),
]