from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),

    # AUTH
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('challenges/', views.challenges_page, name='challenges'),
    path('critical-thinking/', views.critical_thinking, name='critical_thinking'),
    path('career-exploration/', views.career_exploration, name='career_exploration'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('career-assessment/create/', views.create_career_assessment, name='create_career_assessment'),
    path('career-reflection/create/', views.create_career_reflection, name='create_career_reflection'),
    
]