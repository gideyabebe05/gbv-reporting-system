from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('report/', views.report_form, name='report_form'),
    path('reports/', views.report_list, name='report_list'),
]