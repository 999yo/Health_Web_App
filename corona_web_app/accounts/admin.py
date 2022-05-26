from django.contrib import admin
from .models import MedicalHistory, User
admin.site.register(User)
admin.site.register(MedicalHistory)