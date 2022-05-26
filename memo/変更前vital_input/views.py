from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
from accounts.models import MyUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .forms import VitalForm


