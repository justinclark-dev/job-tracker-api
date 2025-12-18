from django.db import models
from .enums import (
  Status, 
  DocumentType, 
  InterviewFormat, 
  InterviewType,
  FollowUpType,
  FollowUpMethod
)
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class JobApplication(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position_title = models.CharField(max_length=100)
    job_description = models.TextField()
    application_url = models.URLField(max_length=500)
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.BOOKMARKED
    )
    date_applied = models.DateField()
    salary_range = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Document(models.Model):
    job_application_id = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    document_type = models.CharField(
        max_length=50,
        choices=DocumentType.choices,
        default=DocumentType.RESUME
    )
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)
    file_size = models.BigIntegerField()
    uploaded_at = models.DateTimeField(auto_now=True)

class Interview(models.Model):
    job_application_id = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    interview_format = models.CharField(
        max_length=6,
        choices=InterviewFormat.choices,
    )
    interview_type = models.CharField(
        max_length=12,
        choices=InterviewType.choices,
    )
    scheduled_date = models.DateTimeField()
    duration_minutes = models.IntegerField()
    interviewer_name = models.CharField(max_length=100)
    notes = models.TextField()
    reminder_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Company(models.Model):
    company_name = models.CharField(100)

class ContactPerson(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(50)
    last_name = models.CharField(50)
    email = models.EmailField(100)
    linkedin = models.URLField(100)
    phone_company = models.CharField(
        # Phone Regex copied from:
        # https://www.geeksforgeeks.org/python/properly-store-and-validate-phone-numbers-in-django-models/#
        # Detailed Explanation:
        # https://claude.ai/share/54aba894-9c37-4f99-8ec0-e2a4c4b6b872
        max_length=20,  # Adjust based on your needs
        validators=[
            RegexValidator(
                # Example regex for international phone numbers
                regex=r'^\+?1?\d{9,15}$',  
                message= (
                  "Phone number must be entered in the format: "
                  "'+999999999'. Up to 15 digits allowed."
                )
            )
        ]
    )

class FollowUp(models.Model):
    job_application_id = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    contact_person_id = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField()
    follow_up_type = models.CharField(
        max_length=16,
        choices=FollowUpType.choices,
    )
    follow_up_method = models.CharField(
        max_length=9,
        choices=FollowUpMethod.choices,
    )
    subject_line = models.CharField(max_length=200)
    message_template = models.TextField()
    notes = models.TextField()
    reminder_sent = models.BooleanField(default=False)
    reminder_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)