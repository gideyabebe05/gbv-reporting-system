import uuid
from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    report_id = models.CharField(max_length=20, unique=True, blank=True, db_index=True)
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)

    INCIDENT_TYPE_CHOICES = [
        ('physical', 'Physical Violence'),
        ('sexual', 'Sexual Violence'),
        ('psychological', 'Psychological / Emotional Abuse'),
        ('economic', 'Economic Abuse'),
        ('harmful_practice', 'Harmful Traditional Practice'),
        ('other', 'Other'),
    ]

    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPE_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    incident_date = models.DateField(null=True, blank=True)

    is_anonymous = models.BooleanField(default=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    consent_to_followup = models.BooleanField(default=False)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.report_id:
            self.report_id = f"GBV-{str(uuid.uuid4())[:8].upper()}"
        if self.is_anonymous:
            self.name = None
            self.phone = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.report_id} - {self.get_incident_type_display()}"

class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('medical', 'Medical'),
        ('legal', 'Legal'),
        ('counseling', 'Counseling'),
        ('shelter', 'Shelter'),
        ('hotline', 'Hotline'),
        ('ngo', 'NGO'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=150)
    type = models.CharField(max_length=50, choices=RESOURCE_TYPE_CHOICES)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)   # Made nullable
    email = models.EmailField(blank=True, null=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']