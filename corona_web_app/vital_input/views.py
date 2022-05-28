from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import Vital
from . import forms
from .forms import VitalForm
from django.views.generic import CreateView


def VitalFormView(request):
  form = VitalForm(request.POST)
  if form.is_valid():
    form.save()
  context = {
    'form': form,
  }
  return render(request, 'vital_input_HTML/vital_input.html', context)
