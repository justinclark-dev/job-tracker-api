from rest_framework import serializers 
from .models import (
    JobApplication,
    Document,
    Interview,
    Company,
    ContactPerson,
    FollowUp
)
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        # tell django which model to use
        model = User 
        # tell django which fields to include
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'last_login',
            'date_joined',
            'is_superuser'
        )

class JobApplicationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = JobApplication 
        fields = (
            'id',
            'user_id', 
            'company_name', 
            'position_title', 
            'job_description', 
            'application_url', 
            'status', 
            'date_applied', 
            'salary_range', 
            'location', 
            'notes', 
            'created_at', 
            'updated_at'
        )

class DocumentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Document 
        fields = (
            'id',
            'job_application_id',
            'document_type',
            'file_name',
            'file_path',
            'file_size',
            'uploaded_at'
        )

class InterviewSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Interview 
        fields = (
            'id',
            'job_application_id',
            'interview_format',
            'interview_type',
            'scheduled_date',
            'duration_minutes',
            'interviewer_name',
            'notes',
            'reminder_sent',
            'created_at',
            'updated_at'
        )

class CompanySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Company 
        fields = (
            'id',
            'company_name'
        )

class ContactPersonSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ContactPerson 
        fields = (
            'id',
            'company_id'
            'first_name'
            'last_name'
            'email'
            'linkedin'
            'phone_company'
        )

class FollowUpSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FollowUp 
        fields = (
            'id',
            'job_application_id',
            'contact_person_id',
            'scheduled_date',
            'completed',
            'completed_date',
            'follow_up_type',
            'follow_up_method',
            'subject_line',
            'message_template',
            'notes',
            'reminder_sent',
            'reminder_date',
            'created_at',
            'updated_at'
        )
