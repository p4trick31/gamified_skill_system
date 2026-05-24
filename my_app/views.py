from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, "home.html")


# SIGNUP FUNCTION

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("landing_page")

        User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        messages.success(request, "Account created successfully!")
        return redirect("landing_page")

    return redirect("landing_page")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful!")

            if user.role == "student":
                return redirect("student_dashboard")
            else:
                return redirect("teacher_dashboard")
                

        messages.error(request, "Invalid username or password")
        return redirect("landing_page")

    return redirect("landing_page")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("landing_page")

def student_dashboard(request):


    return render(request, "student/student_dashboard.html", {
    
    })
@login_required
def teacher_dashboard(request):
   

    return render(request, "teacher/teacher_dashboard.html", {
        
    })

@login_required
def challenges_page(request):
    return render(request, "teacher/challenges_page.html")

@login_required
def critical_thinking(request):
    return render(request, "teacher/critical_thinking.html")

@login_required
def career_exploration(request):
    return render(request, "teacher/career_exploration.html")

@login_required
def create_career_assessment(request):
    return render(request, "teacher/create_career_assessment.html")


@login_required
def create_career_reflection(request):
    return render(request, "teacher/create_career_reflection.html")