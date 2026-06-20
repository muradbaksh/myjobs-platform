from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from .models import User
from django.contrib.auth.decorators import login_required
from reviews.models import CompanyReview
from compensation.models import Compensation
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import email_token
from .forms import ProfileUpdateForm
from django.contrib import messages


# SIMPLIFIED EMAIL VERIFY FLOW
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # MUST VERIFY EMAIL FIRST
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = email_token.make_token(user)

            link = f"http://127.0.0.1:8000/accounts/verify/{uid}/{token}/"

            send_mail(
                "Verify your MYJOBS account",
                f"Click to verify: {link}",
                "noreply@myjobs.com",
                [user.email],
                fail_silently=False,
            )

            print("Verification email sent to:", user.email)
            messages.success(request,"Registration successful. Please verify your email.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})



from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
User = get_user_model()

def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        if email_token.check_token(user, token):
            user.is_active = True
            user.is_verified = True
            user.save()
            messages.success(
                request,
                "Email verified successfully."
            )
            return redirect('login')

    except:
        messages.error(
            request,
            "Verification failed."
        )
    return render(request, 'verify_failed.html')




def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request,"Login Successful.")
            return redirect('profile')
        else:
            messages.error(request,"Invalid username or password.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.warning(
        request,
        "Logout successful."
    )
    return redirect('login')



@login_required
def user_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated successfully.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    reviews = CompanyReview.objects.filter(user=request.user)
    salaries = Compensation.objects.filter(user=request.user)

    return render(request, 'profile.html', {
        'form' : form,
        'reviews': reviews,
        'salaries': salaries
    })



@login_required
def profile_update(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated successfully.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request,'profile_update.html',{'form': form})