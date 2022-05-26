from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegistrationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import *

from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import MedicalHistoryForm,RegistrationForm, UserInformationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import *


class  AccountRegistration(TemplateView):
    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "registration_form": RegistrationForm(),
        "user_information_form":UserInformationForm(),
        }
    def get(self,request):
        self.params["registration_form"] = RegistrationForm()
        self.params["user_information_form"] = UserInformationForm()
        self.params["AccountCreate"] = False
        return render(request,"accounts_HTML/register.html",context=self.params)

    def post(self,request):
        self.params["registration_form"] = RegistrationForm(data=request.POST)
        self.params["user_information_form"] = UserInformationForm(data=request.POST)
        
        if self.params["registration_form"].is_valid() and self.params["user_information_form"].is_valid():
          account = self.params["registration_form"].save()
          self.params["user_information_form"].save()
            #パスワードをハッシュ化
          account.set_password(account.password)
          # ハッシュ化パスワード更新
          account.save()
          self.params["AccountCreate"] = True
        else:
            # フォームが有効でない場合
            print(self.params["registration_form"].errors)
        return render(request,'accounts_HTML/medical_history_create.html',context=self.params)

class MedicalHistoryRegstraion(TemplateView):
    def __init__(self):
        self.params = {
        "MedicalHistoryCreate":False,
        "user_medical_historly_form":MedicalHistoryForm()
        }

    def get(self,request):
        self.params["user_medical_historly_form"] = MedicalHistoryForm()
        self.params["MedicalHistoryCreate"] = False
        return render(request,"accounts_HTML/medical_history_create.html",context=self.params)

    def post(self,request):
        MedicalHistory.user = request.user
        self.params["user_medical_historly_form"] = MedicalHistoryForm(data=request.POST)
        
        # フォーム入力の有効検証
        if self.params["user_medical_historly_form"].is_valid():
          # アカウント情報をDB保存
          self.params["user_medical_historly_form"].save()
          # アカウント作成情報更新
          self.params["MedicalHistoryCreate"] = True
        else:
            # フォームが有効でない場合
            print(self.params["registration_form"].errors)
        return render(request,'accounts_HTML/medical_history_create.html',context=self.params)



######ログイン、新規登録、ログイン後ページ######
#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'accounts_HTML/login_index.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "accounts_HTML/login_home.html",context=params)



#####ログイン、新規登録、ログイン後ページ######
#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')
        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)
        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'accounts_HTML/login_index.html')

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "accounts_HTML/login_home.html",context=params)

    