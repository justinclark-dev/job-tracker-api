# from django.shortcuts import render
from rest_framework import generics
from .serializers import (
    JobApplicationSerializer,
    DocumentSerializer,
    InterviewSerializer,
    CompanySerializer,
    ContactPersonSerializer,
    FollowUpSerializer
)
from .models import (
    JobApplication,
    Document,
    Interview,
    Company,
    ContactPerson,
    FollowUp
)

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
