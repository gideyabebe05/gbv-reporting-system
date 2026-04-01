import uuid
from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):
    """
    Main model for GBV incident reports.
    Supports fully anonymous reporting while allowing
    support organizations to manage and track cases.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    INCIDENT_TYPE_CHOICES = [
        ('physical', 'Physical Violence'),
        ('sexual', 'Sexual Violence'),
        ('psychological', 'Psychological/Emotional Abuse'),
        ('economic', 'Economic Abuse'),
        ('harmful_practice', 'Harmful Traditional Practice'),
        ('other', 'Other'),
    ]

    # Unique tracking ID for survivors to follow up anonymously
    tracking_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )

    # Core report fields
    incident_type = models.CharField(
        max_length=50,
        choices=INCIDENT_TYPE_CHOICES,
        verbose_name="Type of Violence"
    )
    description = models.TextField(verbose_name="Description of the Incident")
    location = models.CharField(
        max_length=255,
        verbose_name="Location (Zone/Woreda in Tigray)"
    )
    incident_date = models.DateField(verbose_name="Date of Incident")

    # Anonymity & contact (optional for follow-up with consent)
    is_anonymous = models.BooleanField(default=True, verbose_name="Report Anonymously")
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Full Name (optional)"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Phone Number (optional)"
    )
    consent_to_followup = models.BooleanField(
        default=False,
        verbose_name="I consent to follow-up contact"
    )

    # Case management fields (visible only to logged-in organizations)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_reports"
    )
    notes = models.TextField(blank=True, null=True, verbose_name="Internal Notes")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "GBV Report"
        verbose_name_plural = "GBV Reports"
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['incident_date']),
        ]

    def __str__(self):
        return f"Report #{self.tracking_id} - {self.get_incident_type_display()} ({self.status})"


class Resource(models.Model):
    """
    Support resources (helplines, organizations, services)
    displayed on the resources.html page.
    """
    RESOURCE_TYPE_CHOICES = [
        ('medical', 'Medical / Health Services'),
        ('legal', 'Legal Aid'),
        ('counseling', 'Psychological Counseling'),
        ('shelter', 'Safe Shelter'),
        ('hotline', 'Emergency Hotline'),
        ('ngo', 'NGO / Support Organization'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=150, verbose_name="Resource Name")
    type = models.CharField(
        max_length=50,
        choices=RESOURCE_TYPE_CHOICES,
        verbose_name="Service Type"
    )
    description = models.TextField(blank=True, verbose_name="Brief Description")
    location = models.CharField(
        max_length=200,
        verbose_name="Location (Tigray Region)"
    )
    phone = models.CharField(max_length=20, verbose_name="Contact Phone")
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Support Resource"
        verbose_name_plural = "Support Resources"

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"