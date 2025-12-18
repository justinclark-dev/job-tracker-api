from django.contrib import admin
from .models import (
    JobApplication,
    Document,
    Interview,
    Company,
    ContactPerson,
    FollowUp
)

admin.site.register(JobApplication)
admin.site.register(Document)
admin.site.register(Interview)
admin.site.register(Company)
admin.site.register(ContactPerson)
admin.site.register(FollowUp)