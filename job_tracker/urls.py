from django.urls import path
from . import views

urlpatterns = [
    # api/job_applications
    # routes to JobApplicationList view for handling
    path('api/job_applications', views.JobApplicationList.as_view(), name='job_application_list'), 
    # routes to JobApplicationDetail view for handling
    path('api/job_applications/<int:pk>', views.JobApplicationDetail.as_view(), name='job_application_detail'), 

    # api/documents
    path('api/documents', views.DocumentList.as_view(), name='document_list'), 
    path('api/documents/<int:pk>', views.DocumentDetail.as_view(), name='document_detail'), 

    # api/interviews
    path('api/interviews', views.InterviewList.as_view(), name='interview_list'), 
    path('api/interviews/<int:pk>', views.InterviewDetail.as_view(), name='interview_detail'), 

    # api/companies
    path('api/companies', views.CompanyList.as_view(), name='company_list'), 
    path('api/companies/<int:pk>', views.CompanyDetail.as_view(), name='companyt_detail'), 

    # api/contacts
    path('api/contacts', views.ContactPersonList.as_view(), name='contact_person_list'), 
    path('api/contacts/<int:pk>', views.ContactPersonDetail.as_view(), name='contact_person_detail'), 

    # api/follow_ups
    path('api/follow_ups', views.FollowUpList.as_view(), name='follow_up_list'), 
    path('api/follow_ups/<int:pk>', views.FollowUpDetail.as_view(), name='follow_up_detail'), 
]