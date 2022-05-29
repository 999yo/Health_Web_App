from xml.etree.ElementInclude import include
from django.urls import path
from . import views
app_name = 'data_tables_view'
urlpatterns = [
  path('data_search', views.BaseDatatableView.as_view(), name= 'data_search'),
  path('datalist', views.UserInformationList.as_view(), name='datalist'),
  path('data_search_ajax/', views.UserInformationJsonView.as_view(), name='booklist_ajax'),
  path('datadetail/<int:pk>', views.UserInformationDetail.as_view(), name='datadetail'),
]