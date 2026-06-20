from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:id>/', views.add_salary, name='add_salary'),
    path('benchmark/',views.benchmark,name='benchmark'),
]