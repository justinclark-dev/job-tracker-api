# from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import (
    JobApplication,
    Document,
    Interview,
    Company,
    ContactPerson,
    FollowUp
)
from .serializers import (
    UserSerializer,
    JobApplicationSerializer,
    DocumentSerializer,
    InterviewSerializer,
    CompanySerializer,
    ContactPersonSerializer,
    FollowUpSerializer
)
# for building API endpoint to get enums for the UI
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .enums import Status  # Import the Status enum

# User
class UserList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = User.objects.all().order_by('id') 
    # tell django what serializer to use
    serializer_class = UserSerializer 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

# Job Application
class JobApplicationList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = JobApplication.objects.all().order_by('id') 
    # tell django what serializer to use
    serializer_class = JobApplicationSerializer 

class JobApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all().order_by('id')
    serializer_class = JobApplicationSerializer
  
# Document
class DocumentList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Document.objects.all().order_by('id') 
    # tell django what serializer to use
    serializer_class = DocumentSerializer 

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all().order_by('id')
    serializer_class = DocumentSerializer

# Interview
class InterviewList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Interview.objects.all().order_by('id') 
    # tell django what serializer to use
    serializer_class = InterviewSerializer 

class InterviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interview.objects.all().order_by('id')
    serializer_class = InterviewSerializer

# Company
class CompanyList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Company.objects.all().order_by('id') 
    # tell django what serializer to use
    serializer_class = CompanySerializer 

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer

# Contact Person
class ContactPersonList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = ContactPerson.objects.all().order_by('id') 
    # tell django what serializer to use
    serializer_class = ContactPersonSerializer 

class ContactPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactPerson.objects.all().order_by('id')
    serializer_class = ContactPersonSerializer

# Follow Up
class FollowUpList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = FollowUp.objects.all().order_by('id') 
    # tell django what serializer to use
    serializer_class = FollowUpSerializer 

class FollowUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FollowUp.objects.all().order_by('id')
    serializer_class = FollowUpSerializer


# ENUM FUNCTIONS (to make enpoints to get enum values for the UI dropdowns)
# https://www.django-rest-framework.org/api-guide/views/#function-based-views
# marks the function as an API endpoint
@api_view(['GET'])
# defines a view function that takes an HTTP request as a parameter
def get_status_choices(request):
    # returns a JSON response containing a list of status choices. 
    # The list comprehension iterates through Status.choices
    # and creates a dictionary for each one.
    return Response({
        'choices': [
            {'value': value, 'label': label} 
            for value, label in Status.choices
        ]
    })
