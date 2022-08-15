
from django.urls import path
from . import views

urlpatterns = [
  path('health_care', views.check, name = 'health_care')
  ]