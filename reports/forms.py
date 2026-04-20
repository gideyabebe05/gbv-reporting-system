from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'incident_type',
            'description',
            'location',
            'incident_date',
            'is_anonymous',
            'name',
            'phone',
            'consent_to_followup',
        ]
        widgets = {
            'incident_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={
                'rows': 5, 
                'placeholder': 'Describe the incident...'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        # Ensure anonymous reporting clears name and phone
        if cleaned_data.get('is_anonymous'):
            cleaned_data['name'] = None
            cleaned_data['phone'] = None

        return cleaned_data
