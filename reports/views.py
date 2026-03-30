def submit_report(request):
    if request.method == 'POST':
        incident_type = request.POST.get('incident_type')
        description = request.POST.get('description')
        location = request.POST.get('location')

        is_anonymous = request.POST.get('is_anonymous') == 'on'

        name = request.POST.get('name')
        phone = request.POST.get('phone')

        if is_anonymous:
            name = "Anonymous"
            phone = None

        report = Report.objects.create(
            incident_type=incident_type,
            description=description,
            location=location,
            is_anonymous=is_anonymous,
            name=name,
            phone=phone
        )

        return render(request, 'reports/success.html', {
            'tracking_id': report.tracking_id
        })

    return redirect('report_form')
