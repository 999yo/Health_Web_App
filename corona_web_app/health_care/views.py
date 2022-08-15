from django import forms
from django.shortcuts import render
from . import forms
from django.template.context_processors import csrf

def Health_check(request):
    symptoms = request.POST.get("symptom")
    return render(request, 'health_care_HTML\health_care.html')

