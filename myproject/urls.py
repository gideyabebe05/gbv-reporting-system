from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reports.urls')),   # This will connect all your report pages
]
from django.shortcuts import redirect

path('', lambda request: redirect('reports:report_form')),
