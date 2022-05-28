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


class VitalFormView(TemplateView):
  def __init__(self):
    self.params = {"Message": "以下の健康状態を入力してください",
                  "form": forms.VitalForm}
  
  def get(self, request):
    return render(request, "vital_input_HTML/vital_input.html", context = self.params)

  def post(self, request):
    if request.method == "POST":
      self.params["form"] = forms.VitalForm(request.POST)
      
      if self.params["form"].is_valid():
        self.params["form"].save(commit =True)
        self.params["Message"] = "入力した健康状態が送信されました"
    return render(request,"vital_input_HTML/vital_input.html", context = self.params)