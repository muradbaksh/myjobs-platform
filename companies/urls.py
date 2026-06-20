from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_company,name='add_company'),
    path('<int:id>/', views.company_detail, name='company_detail'),
]