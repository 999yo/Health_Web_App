from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.contrib.auth import get_user_model

class Vital(models.Model):
  vital_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user_vital',null=True)
  vital_date = models.DateTimeField(default=timezone.now)
  BodyTemperature = models.FloatField(validators=[MinValueValidator(30.0), MaxValueValidator(50.0)])
  SpO2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
  Sbp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)]) #収縮期血圧
  Dbp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)]) #拡張期血圧
  Pulse = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)])

  CHOICES = [('無', 'なし'),('少し','少しある'),('有','ある'),('不明','分からない')]
  Dyspnea = models.TextField(verbose_name = "息苦しさ", choices= CHOICES,blank=True)
  ChestPain = models.TextField(verbose_name = "胸の痛み", choices= CHOICES,blank=True)
  Fatigue = models.TextField(verbose_name = "倦怠感（だるさ）", choices= CHOICES,blank=True)
  Chills = models.TextField(verbose_name = "悪寒", choices= CHOICES,blank=True)
  Cough = models.TextField(verbose_name = "咳", choices= CHOICES,blank=True)
  RunnyNose = models.TextField(verbose_name = "鼻水", choices= CHOICES,blank=True)
  Nausea = models.TextField(verbose_name = "嘔気", choices= CHOICES,blank=True) 
  Vomiting = models.TextField(verbose_name = "嘔吐", choices= CHOICES,blank=True)
  Diarrhea = models.TextField(verbose_name = "下痢", choices= CHOICES,blank=True)
  Headache = models.TextField(verbose_name = "頭痛", choices= CHOICES,blank=True)
  Stomachace = models.TextField(verbose_name = "腹痛", choices= CHOICES,blank=True)
  JointPain = models.TextField(verbose_name = "関節痛", choices= CHOICES,blank=True)
  Dysosmia = models.TextField(verbose_name = "嗅覚異常", choices= CHOICES,blank=True)
  Dysgeusia = models.TextField(verbose_name = "味覚異常", choices= CHOICES,blank=True)
  Convulsion = models.TextField(verbose_name = "けいれん", choices= CHOICES,blank=True)

  APPETITE_CHOICE = [('有', 'ある'),('少し','少しある'),('無','なし'),('不明','分からない')]
  MEAL_AMOUNT_CHOICE = [('0','いつも通り'),('1', 'いつもより少ないが、食べれている'),('2','全く食べれていない'),('3','不明')]
  AMOUNT_OF_WATER_CHOICE = [('0', '1L以上'),('1','500ml~1L'),('2','500ml未満'),('3','不明')]
  ANTIPYRETICS_CHOICE = [('0', '6回分以上'),('1', '3~5回分'),('2', '持っていない')]

  LossOfAppetite = models.TextField(verbose_name = "食欲", choices= APPETITE_CHOICE,blank=True) 
  MealAmount = models.TextField(verbose_name = "食事量", choices= MEAL_AMOUNT_CHOICE,blank=True) 
  AmountOfWater = models.TextField(verbose_name = "水分量", choices= AMOUNT_OF_WATER_CHOICE,blank=True)
  NumberOfAntipyretics = models.TextField(verbose_name = "解熱剤の残数", choices= ANTIPYRETICS_CHOICE,blank=True)

  def __str__(self):
    return self.vital_date




