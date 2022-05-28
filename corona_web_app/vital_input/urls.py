from django.urls import path
from . import views

urlpatterns = [
  path('vital_input', views.VitalFormView, name = 'vital_input')
]