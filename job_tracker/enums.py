# https://pythonguides.com/python-django-get-enum-choices/

from django.db import models

class Status(models.TextChoices):
    BOOKMARKED = 'bookmarked', 'BOOKMARKED'
    APPLYING = 'applying', 'APPLYING'
    APPLIED = 'applied', 'APPLIED'
    INTERVIEWING = 'interviewing','INTERVIEWING'
    OFFER = 'offer', 'OFFER'
    REJECTED = 'rejected', 'REJECTED'

class DocumentType(models.TextChoices):
    RESUME = 'resume', 'RESUME'
    COVER_LETTER = 'cover_letter', 'COVER_LETTER'
    OTHER = 'other', 'OTHER'

class InterviewFormat(models.TextChoices):
    PHONE = 'phone', 'PHONE'
    VIDEO = 'video', 'VIDEO'
    ONSITE = 'onsite', 'ONSITE'

class InterviewType(models.TextChoices):
    PHONE_SCREEN = 'phone_screen', 'PHONE_SCREEN'
    ONE_ON_ONE = 'one_on_one', 'ONE_ON_ONE'
    GROUP = 'group', 'GROUP'

class FollowUpType(models.TextChoices):
    POST_APPLICATION = 'post_application', 'POST_APPLICATION'
    POST_INTERVIEW = 'post_interview', 'POST_INTERVIEW'
    THANK_YOU = 'thnak_you', 'THANK_YOU'
    CHECK_IN = 'check_in', 'CHECK_IN'
    NETWORKING = 'networking', 'NETWORKING'

class FollowUpMethod(models.TextChoices):
    EMAIL = 'email', 'EMAIL'
    PHONE = 'phone', 'PHONE'
    LINKEDIN = 'linkedin', 'LINKEDIN'
    IN_PERSON = 'in_person', 'IN_PERSON'