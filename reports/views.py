from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Report, Resource
from .forms import ReportForm


def report_form(request):
    """Anonymous GBV Reporting Page"""
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            if report.is_anonymous:
                report.name = None
                report.phone = None
            report.save()

            messages.success(request, f'✅ Report submitted successfully! Your tracking ID is: {report.tracking_id}')
            return render(request, 'reports/success.html', {'tracking_id': report.tracking_id})
    else:
        form = ReportForm()

    return render(request, 'reports/report_form.html', {'form': form})


def report_list(request):
    """Case management for organizations"""
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'reports/report_list.html', {'reports': reports})


def resources_view(request):
    """Support resources page"""
    resources = Resource.objects.filter(is_active=True)
    return render(request, 'reports/resources.html', {'resources': resources})