from django.utils import timezone
from traitlets import default
from django.db import models

class HealthCare(models.Model):
    date = models.DateField(default=timezone.now)
    