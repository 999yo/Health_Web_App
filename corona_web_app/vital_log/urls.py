from django.urls import path
from . import views

urlpatterns = [
  path('vital_log', views.vital_log, name='vital_log')
]