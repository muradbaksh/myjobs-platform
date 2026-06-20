from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    # path('verify/<uidb64>/<token>/', views.verify_email, name='verify_email'),
    
    path('profile-update/',views.profile_update,name='profile_update'),
    path('password-change/',auth_views.PasswordChangeView.as_view(template_name='password_change.html'),name='password_change'),
    path('password-change-done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),
]
