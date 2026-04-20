from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'reports'

urlpatterns = [
    # 🌐 HOME
    path('', views.home, name='home'),

    # 🔴 PUBLIC PAGES
    path('report/', views.report_form, name='report_form'),
    path('report/success/<str:tracking_id>/', views.report_success, name='report_success'),
    path('track/', views.track_report, name='track_report'),
    path('resources/', views.resources_view, name='resources'),

    # 🔐 AUTHENTICATION
    path('login/', LoginView.as_view(template_name='reports/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='reports:login'), name='logout'),

    # 🏢 DASHBOARD (Fixed - now accessible at /reports/)
    path('reports/', views.report_list, name='report_list'),

    # 📄 REPORT DETAIL & UPDATE
    path('report/<int:pk>/', views.report_detail, name='report_detail'),
    path('report/update/<int:pk>/', views.update_report, name='update_report'),
    
]