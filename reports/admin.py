from django.contrib import admin
from .models import Report, Resource


# ===============================
# REPORT ADMIN (Safe & Clean)
# ===============================
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'tracking_id', 'incident_type', 'status', 'location', 'created_at')
    list_filter = ('status', 'incident_type', 'is_anonymous')
    search_fields = ('report_id', 'tracking_id', 'description', 'location', 'name')
    readonly_fields = ('report_id', 'tracking_id', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Report Information', {
            'fields': ('report_id', 'tracking_id', 'incident_type', 'description', 'location', 'incident_date')
        }),
        ('Reporter Details', {
            'fields': ('is_anonymous', 'name', 'phone', 'consent_to_followup')
        }),
        ('Case Management', {
            'fields': ('status', 'assigned_to', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# ===============================
# RESOURCE ADMIN
# ===============================
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location', 'phone', 'is_active')
    list_filter = ('type', 'is_active')
    search_fields = ('name', 'location', 'phone')
    ordering = ('name',)


# Admin Site Title
admin.site.site_header = "Tigray GBV Support System - Administration"
admin.site.site_title = "Tigray GBV Admin"
admin.site.index_title = "Welcome to GBV Case Management"