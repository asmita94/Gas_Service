from django.db import models
from django.contrib.auth.models import User

# class ServiceRequest(models.Model):
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('In Progress', 'In Progress'),
#         ('Resolved', 'Resolved'),
#     ]
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=100)
#     details = models.TextField()
#     attachment = models.FileField(upload_to='attachments/')
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     resolved_at = models.DateTimeField(null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields like address, phone_number, etc.


class ServiceRequest(models.Model):
    requester_name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    request_type = models.CharField(max_length=50, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.requester_name
