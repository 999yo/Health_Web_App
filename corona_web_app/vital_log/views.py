from dataclasses import field
from django.shortcuts import render
from vital_input.models import Vital
import numpy as np
import pandas as pd
from django_pandas.io import read_frame
from django.contrib.auth.decorators import login_required
#from .graph import GraphGenerator
####グラフ
import io

#plotly
from vital_input.models import Vital
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import pandas
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import sqlite3
from plotly.offline import plot


@login_required
def vital_log(request):
  data = Vital.objects.all()
  params = {'message': '', 'data':data, 'username':request.user.last_name}
  return render(request,'vital_log_HTML/vital_log.html',params)

@login_required
def first_vital_log(request):
  first_data = Vital.objects.get(id=1)
  params = {'first_data':first_data}
  return render(request,'vital_log_HTML/vital_log.html',params)

@login_required
def home(request):
    params = {"UserID":request.user.last_name}
    return render(request, "accounts_HTML/login_home.html",context=params)
