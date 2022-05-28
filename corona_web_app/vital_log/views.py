from django.views.generic import DetailView, ListView
from django_datatables_view.base_datatable_view import BaseDatatableView
from vital_input.models import Vital
from django.urls import reverse_lazy

class VitalList(ListView):
    model = Vital
    template_name = 'vital_log_HTML/vital_log.html'

class VitalJsonView(BaseDatatableView):
    model = Vital
    success_url = reverse_lazy('vital_log')
    
    columns = ['vital_date', 'BodyTemperature', 'SpO2', 'Sbp', 'Dbp', 
    'Pulse', 'Dyspnea', 'ChestPain', 'Fatigue', 'Chills','Cough', 'RunnyNose','Nausea', 'Vomiting', 'Diarrhea', 
    'Headache','Stomachace','JointPain','Dysosmia', 'Dysgeusia', 'Convulsion', 'LossOfAppetite', 'MealAmount', 'AmountOfWater', 'NumberOfAntipyretics']
    def render_column(self, row, column):
        if column == 'id':
            return f'<a href="/vital_log_HTML/vital_detail/{row.id}">{row.id}</a>'
        else:
            return super(VitalJsonView, self).render_column(row, column)

    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

class VitalDetail(DetailView):
    model = Vital
    template_name = 'vital_log_HTML/Vital_detail.html'

import pandas
import plotly.graph_objects as go
import sqlite3
from django.views.generic import TemplateView

def vital_graph():
  
  conn = sqlite3.connect('db.sqlite3')
  df = pandas.read_sql_query('SELECT * FROM vital_input_vital',conn)
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=df["vital_date"], 
              y=df["BodyTemperature"],
              mode='markers+lines+text',
              textposition='top right',
              texttemplate='%{y:}℃',
              textfont=dict(size=10),
              name="体温", line=dict(color="#FFA15A")))
  fig.add_trace(go.Scatter(x=df["vital_date"], 
              y=df["SpO2"],
              mode='markers+lines+text',
              textposition='bottom left',
              texttemplate='%{y:}%',
              textfont=dict(size=10),
              name="SpO2",
              line=dict(color="#72B7B2"),
              yaxis="y2"))
  fig.add_trace(go.Scatter(x=df["vital_date"], 
              mode='markers+lines+text',
              textposition='top center',
              texttemplate='%{y:}mmHg',
              textfont=dict(size=10),
              y=df["Sbp"], name="収縮期血圧",
              line=dict(color="#fbb4ae"), 
              yaxis="y3"))
  fig.add_trace(go.Scatter(x=df["vital_date"], 
              mode='markers+lines+text',
              textposition='bottom center',
              texttemplate='%{y:}mmHg',
              textfont=dict(size=10),
              y=df["Dbp"], 
              name="拡張期血圧",
              line=dict(color="#b3cde3"),yaxis="y4"))


  # Create axis objects
  fig.update_layout(
    xaxis=dict(
      domain=[0, 1]
    ),
    #体温
    yaxis=dict( domain=[0, 1],
      title="", titlefont=dict(color="#FFA15A"),
      tickfont=dict(color="#FFA15A")),
    
    #酸素飽和度
    yaxis2=dict(
      title="SpO2",
      titlefont=dict(color="#72B7B2"),
      tickfont=dict(color="#72B7B2"),
      anchor="free", overlaying="y",
      side="left", position=1),
    yaxis3=dict(
      title="Sbp",
      titlefont=dict(color="#fbb4ae"),
      tickfont=dict(color="#fbb4ae"),
      anchor="x", overlaying="y", side="left",position=0.3),

    yaxis4=dict(
      title="Dbp",
      titlefont=dict(color="#b3cde3"),
      tickfont=dict(color="#b3cde3"),
      anchor="free", overlaying="y",
      side="right", position=1)
  )

  # Update layout properties
  fig.update_layout(
    title_text="検温表",
    
  )

  conn.close()
  return fig.to_html(include_plotlyjs=False)

class VitalGraphView(TemplateView):
  template_name = "vital_log_HTML/vital_log.html"

  def get_context_data(self, **kwargs):
    context = super(VitalGraphView, self).get_context_data(**kwargs)
    context["vital_plot"] = vital_graph()
    return context
