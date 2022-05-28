from django.urls import path
from . import views

urlpatterns = [
  path('vital_input', views.VitalFormView.as_view(), name = 'vital_input')
]