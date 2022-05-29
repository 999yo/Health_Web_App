from django.contrib import admin
from .models import MedicalHistory, User, CoronaHistory
admin.site.register(User)
admin.site.register(MedicalHistory)
admin.site.register(CoronaHistory)
