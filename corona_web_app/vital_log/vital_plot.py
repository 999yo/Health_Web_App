#from vital_input.models import Vital
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import sqlite3
import pandas as pd 
from plotly.offline import plot


conn = sqlite3.connect('corona_app_project.sqlite3')
df = pd.read_sql_query('SELECT * FROM vital_input',conn)
#cur.execute('SELECT * FROM vital_input')
#データベースとの連携
#with sqlite3.connect('corona_app_project.sqlite3') as engine:
    #df = pd.read_sql('SELECT * FROM vital_input',engine)

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
  yaxis=dict(
    title="", titlefont=dict(color="#FFA15A"),
    tickfont=dict(color="#FFA15A")),

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
  width=800,
)


fig.show()
fig.write_html("template/vitalgraph.html")
conn.close()