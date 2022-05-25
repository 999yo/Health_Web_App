from dataclasses import field
from django.shortcuts import render
from vital_input.models import Vital
import numpy as np
import pandas as pd
from django_pandas.io import read_frame
#from .graph import GraphGenerator

#plotly
from vital_input.models import Vital
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def vital_log(request):
  data = Vital.objects.all()
  params = {'message': 'あなたの過去の健康記録', 'data':data}
  return render(request,'vital_log_HTML/vital_log.html',params)

def first_vital_log(request):
  first_data = Vital.objects.get(id=1)
  params = {'first_data':first_data}
  return render(request,'vital_log_HTML/vital_log.html',params)
  