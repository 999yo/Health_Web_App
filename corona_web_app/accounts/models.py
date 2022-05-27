from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError('Emailを入力して下さい')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=Trueである必要があります。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=Trueである必要があります。')
        return self._create_user(email, password, **extra_fields)
 
        
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email_address"), unique=True,null=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    last_name = models.CharField(verbose_name='苗字',max_length=50)
    first_name = models.CharField(verbose_name='名前',max_length=50) 
    last_name_kana = models.CharField(verbose_name='苗字のふりがな',max_length=50)
    first_name_kana = models.CharField(verbose_name='名前のふりがな',max_length=50)
    birthday = models.DateField(verbose_name="生年月日",null=True)
    sex = models.CharField(('性別'), max_length=4, choices=(('男性','男性'), ('女性','女性')))
    height = models.IntegerField(verbose_name='身長',null=True)
    weight = models.IntegerField(verbose_name='体重',null=True)
    phone_number = models.IntegerField(verbose_name='電話番号',null=True)
    postal_code = models.IntegerField(verbose_name="郵便番号",null=True)
    prefecture = models.CharField(verbose_name='都道府県',max_length=50)
    city = models.CharField(verbose_name='市区町村群',max_length=50)
    addressline1 = models.CharField(verbose_name='丁・番地・号',max_length=50)
    building = models.CharField(verbose_name='建物名・部屋番号',max_length=50)
    emargency_contact_number = models.IntegerField(verbose_name='緊急連絡先(番号)',null=True)
    emargency_person = models.CharField(verbose_name='緊急連絡先（名前）',max_length=50,null=True)
    
    def __str__(self):
        return str.email

    objects = UserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    #REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'User'
        verbose_name = _('user')
        verbose_name_plural = _('ユーザー')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.last_name, self.first_name)
        return full_name.strip()

    def get_full_name_kana(self):
        full_name_kana = '%s %s' % (self.last_name_kana, self.first_name_kana)
        return full_name_kana.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)  
    
class MedicalHistory(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user_medical')
    ANSWER_CHOICE =(
        ('なし','なし'),
        ('あり','あり'))
    heart_disease = models.CharField(verbose_name='心疾患（現在治療要の）', choices= ANSWER_CHOICE, max_length=50)
    cirrhosis = models.CharField(verbose_name='肝硬変', choices= ANSWER_CHOICE, max_length=50)
    diabetes = models.CharField(verbose_name='糖尿病', choices= ANSWER_CHOICE, max_length=50)
    chronic_respiratory_disease = models.CharField(verbose_name='慢性呼吸器疾患（気管支喘息含む）', choices= ANSWER_CHOICE, max_length=50)
    kidoney_disease = models.CharField(verbose_name='高度慢性腎臓病（GFR30未満が目安）', choices= ANSWER_CHOICE, max_length=50)
    dialysis = models.CharField(verbose_name='透析', choices= ANSWER_CHOICE, max_length=50)
    malignant_tumor = models.CharField(verbose_name='治療中の悪性腫瘍', choices= ANSWER_CHOICE, max_length=50)
    immune_lowered_state = models.CharField(verbose_name='免疫低下状態', choices= ANSWER_CHOICE, max_length=50)
    pregnant = models.CharField(verbose_name='37週以降の妊婦', choices=(('いいえ','いいえ'),('はい','はい')), max_length=50)
    vaccination_history = models.CharField(verbose_name='ワクチンの接種歴', choices=(('0','打ってない'), ('1','1回'),('2','2回') ,('3','3回')), max_length=50)
    smoking_history = models.CharField(verbose_name='喫煙歴', choices= ANSWER_CHOICE, max_length=50)
    day_smoking = models.CharField(verbose_name='喫煙本数/日', choices=(('0','なし'), 
                                                                        ('10','10本以下'),
                                                                        ('30','10-30本'),
                                                                        ('50','50本以上')), max_length=50)
    year_smoking = models.CharField(verbose_name=('喫煙年数'), choices=(('0','なし'), 
                                                                        ('10','10年未満'),
                                                                        ('20','20年以上'),
                                                                        ('30','30年以上'),
                                                                        ('40','40年以上'),
                                                                        ('50','50年以上')), max_length=50)

    class Meta:
        db_table = 'User_medical_history'
        verbose_name = _('既往歴')
        verbose_name_plural = _('既往歴')

class CoronaHistory(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user_corona_history')
    #発症日
    date_of_symptom_onset = models.DateField(verbose_name= '発症日', null=True )
    #検査陽性日
    date_of_positive = models.DateField(verbose_name= '検査陽性日', null=True )
    
    class Meta:
        db_table = 'user_corona_history'
        verbose_name = _('発症日と陽性日')

