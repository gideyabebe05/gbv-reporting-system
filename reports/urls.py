
from django.urls import path
from . import views

app_name = 'reports'   # important for namespacing

urlpatterns = [
    path('report/', views.report_form, name='report_form'),
    path('success/', views.success, name='success'),
    path('reports/', views.report_list, name='report_list'),
    path('login/', views.login_view, name='login'),
    path('resources/', views.resources, name='resources'),
    # you can add more later (detail view, etc.)
]