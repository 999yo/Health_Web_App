from django.urls import path
from . import views

app_name = 'vital_log'
urlpatterns = [
  path('vital_list/', views.VitalList.as_view(), name='vital_list'),
  path('vital_list_ajax/', views.VitalJsonView.as_view(), name='vital_list_ajax'),
  path('vitaldetail/<int:pk>', views.VitalDetail.as_view(), name='vitaldetail'),
  path('vital_plot', views.VitalGraphView.as_view(), name = 'vital_plot')
]