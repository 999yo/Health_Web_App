from django.urls import path
from . import views

app_name = 'vital_log_app'
urlpatterns = [
  path('vital_log', views.VitalList.as_view(), name='vital_log'),
  path('vital_list_ajax/', views.VitalJsonView.as_view(), name='vital_list_ajax'),
  path('vitaldetail/<int:pk>', views.VitalDetail.as_view(), name='vitaldetail'),
  path('vital_log', views.VitalGraphView.as_view(), name = 'vital_plot')
]