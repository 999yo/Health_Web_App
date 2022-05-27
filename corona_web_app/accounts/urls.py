from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name = 'Login'), #ログイン前トップページ
    path('registration', views.AccountRegistration.as_view(), name='user_base_information'),
    path('registration2',views.MedicalAndCoronaHistoryRegstraion.as_view(), name='medical_and_corona_history'),
    path("home",views.home,name="home"), #ログイン後home
    path("logout",views.Logout,name="Logout"),
]