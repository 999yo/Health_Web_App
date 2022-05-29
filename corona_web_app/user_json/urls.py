from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'user_table'
urlpatterns = [
    path('user_json_serach', views.UserList.as_view(), name = 'users_data'),
    path('json', views.UserJsonView.as_view(), name='json_data'),
    
]