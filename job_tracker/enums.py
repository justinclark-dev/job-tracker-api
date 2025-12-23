# https://pythonguides.com/python-django-get-enum-choices/

from django.db import models

class Status(models.TextChoices):
    BOOKMARKED = 'bookmarked', 'Bookmarked'
    APPLYING = 'applying', 'Applying'
    APPLIED = 'applied', 'Applied'
    INTERVIEWING = 'interviewing','Interviewing'
    OFFER = 'offer', 'Offer'
    REJECTED = 'rejected', 'Rejected'

class DocumentType(models.TextChoices):
    RESUME = 'resume', 'Resume'
    COVER_LETTER = 'cover_letter', 'Cover Letter'
    OTHER = 'other', 'Other'

class InterviewFormat(models.TextChoices):
    PHONE = 'phone', 'Phone'
    VIDEO = 'video', 'Video'
    ONSITE = 'onsite', 'On-site'

class InterviewType(models.TextChoices):
    PHONE_SCREEN = 'phone_screen', 'Phone Screen'
    ONE_ON_ONE = 'one_on_one', 'One-on-One'
    GROUP = 'group', 'Group'

class FollowUpType(models.TextChoices):
    POST_APPLICATION = 'post_application', 'Post-Application'
    POST_INTERVIEW = 'post_interview', 'Post-Interview'
    THANK_YOU = 'thnak_you', 'Thnak You'
    CHECK_IN = 'check_in', 'Check-In'
    NETWORKING = 'networking', 'Networking'

class FollowUpMethod(models.TextChoices):
    EMAIL = 'email', 'Email'
    PHONE = 'phone', 'Phone'
    LINKEDIN = 'linkedin', 'LinkedIn'
    IN_PERSON = 'in_person', 'In-Person'