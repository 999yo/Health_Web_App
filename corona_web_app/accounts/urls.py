from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name = 'Login'), #ログイン前トップページ
    path('registration', views.AccountRegistration.as_view(), name='registration'),
    path("home",views.home,name="home"), #ログイン後home
    path("logout",views.Logout,name="Logout"),
]