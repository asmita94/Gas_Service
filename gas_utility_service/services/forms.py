from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    # Define choices for the status field
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    # Define choices for the request types field
    REQUEST_TYPES_CHOICES = [
        ('Gas Leak', 'Gas Leak'),
        ('Meter Reading', 'Meter Reading'),
        ('Connection Issue', 'Connection Issue'),
    ]

    # Override the status field to use the defined choices
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    # Add a new field for request types
    request_type = forms.ChoiceField(choices=REQUEST_TYPES_CHOICES)

    class Meta:
        model = ServiceRequest
        fields = ['requester_name','request_type','status' ,'description']
