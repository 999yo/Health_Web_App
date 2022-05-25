from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MedicalHistory, User

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'email'}),
        label="メールアドレス")
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name':'password1'}),
        label="パスワード")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password2'}),
        label="パスワード(確認)")

    class Meta:
        model = User
        fields = ['email','password1','password2']
        field_order = ['email','password1','password2']

class UserInformationForm(forms.ModelForm):
  class Meta():
    model = User
    fields =('last_name', 'first_name', 'last_name_kana', 'first_name_kana', 'birthday',
    'sex','height', 'weight', 'phone_number', 'postal_code', 'prefecture', 'city', 'addressline1','building','emargency_contact_number','emargency_person')
    #widgets={'user':forms.HiddenInput()}

    labels = {
    'last_name': '苗字',
    'first_name': '名前',
    'last_name_kana': '苗字のふりがな',
    'first_name_kana': '名前のふりがな',
    'birthday': '生年月日',
    'sex': '性別',
    'height': '身長',
    'weight': '体重',
    'phone_number': '電話番号',
    'postal_code': '郵便番号',
    'prefecture': '都道府県',
    'city': '市区町村群',
    'addressline1': '丁・番地・号',
    'building': '建物名・部屋番号',
    'emargency_contact_number': '緊急連絡先(番号)',
    'emargency_person': '緊急連絡先（名前）',   
    }


class MedicalHistoryForm(forms.ModelForm):
  class Meta:
    model = MedicalHistory
    fields ='__all__'
    #widgets={'user':forms.HiddenInput()}
    labels = {'heart_disease' :'現在治療が必要または治療中の心疾患',
    'cirrhosis': '肝硬変',
    'diabetes': '糖尿病',
    'chronic_respiratory_disease': '慢性呼吸器疾患（気管支喘息含む）',
    'kidoney_disease': '高度慢性腎臓病（GFR30未満が目安）',
    'dialysis': '透析',
    'malignant_tumor': '治療中の悪性腫瘍',
    'immune_lowered_state': '免疫低下状態',
    'pregnant': '37週以降の妊婦',
    'vaccination_history': 'ワクチンの接種歴',
    'smoking_history': '喫煙歴',
    'day_smoking': '喫煙本数/日',
    'year_smoking': '喫煙年数',
    }