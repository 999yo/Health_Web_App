from .models import Vital
from django.forms import widgets
from django import forms

class VitalForm(forms.ModelForm):
  class Meta():
    model = Vital
    fields = (
      'vital_date', 'BodyTemperature', 'SpO2', 'Sbp', 'Dbp',
      'Pulse','Dyspnea', 'ChestPain', 'Fatigue', 'Chills',
      'Cough', 'Cough', 'RunnyNose','Nausea','Vomiting',
      'Diarrhea', 'Headache', 'Stomachace', 'JointPain', 'Dysosmia',
      'Convulsion','LossOfAppetite','MealAmount', 'AmountOfWater', 'NumberOfAntipyretics')
    labels = {'vital_date':'日時（過去の記録ならその時間を記載してください）',
              'BodyTemperature':'体温',
              'SpO2':'酸素飽和度(SpO2)',
              'Sbp':'収縮期血圧（上の血圧）',
              'Dbp':'拡張期血圧(下の血圧)',
              'Pulse':'脈拍',
              'Dyspnea':"息苦しさ",
              'ChestPain':"胸の痛み",
              'Fatigue':"倦怠感（だるさ）",
              'Chills':"悪寒",
              'Cough':"咳", 
              'RunnyNose':"鼻水", 
              'Nausea':"嘔気",
              'Vomiting':"嘔吐",
              'Diarrhea':"下痢",
              'Headache':"頭痛",
              'Stomachace':"腹痛",
              'JointPain':"関節痛",
              'Dysosmia': "嗅覚異常",
              'Dysgeusia':"味覚異常",
              'Convulsion': "けいれん",
              'LossOfAppetite':"食欲",
              'MealAmount':"食事量",
              'AmountOfWater':"水分量",
              'NumberOfAntipyretics':"解熱剤の残数"
              }
    Widget = {'vital_date': widgets.SplitDateTimeWidget}