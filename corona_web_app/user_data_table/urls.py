from django.urls import path
from django.views.generic.base import TemplateView
from . import views

#app_name = 'user_data_table_app'

urlpatterns = [
    path('user_search', TemplateView.as_view(template_name='user_data_table_HTML/user_data_table.html'), name='user_data_app'),
    path('userjson/', views.some_view, name='UserJson'),
    path('print', views.PrintView.as_view(), name='print'),
    path('excel', views.ExcelView.as_view(), name='excel'),
    path('csv', views.CsvView.as_view(), name='csv'),
]

