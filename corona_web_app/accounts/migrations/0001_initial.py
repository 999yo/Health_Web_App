# Generated by Django 4.0.4 on 2022-05-25 12:48

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email_address')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('last_name', models.CharField(max_length=50, verbose_name='苗字')),
                ('first_name', models.CharField(max_length=50, verbose_name='名前')),
                ('last_name_kana', models.CharField(max_length=50, verbose_name='苗字のふりがな')),
                ('first_name_kana', models.CharField(max_length=50, verbose_name='名前のふりがな')),
                ('birthday', models.DateField(null=True, verbose_name='生年月日')),
                ('sex', models.CharField(choices=[('男性', '男性'), ('女性', '女性')], max_length=4, verbose_name='性別')),
                ('height', models.IntegerField(null=True, verbose_name='身長')),
                ('weight', models.IntegerField(null=True, verbose_name='体重')),
                ('phone_number', models.IntegerField(null=True, verbose_name='電話番号')),
                ('postal_code', models.IntegerField(null=True, verbose_name='郵便番号')),
                ('prefecture', models.CharField(max_length=50, verbose_name='都道府県')),
                ('city', models.CharField(max_length=50, verbose_name='市区町村群')),
                ('addressline1', models.CharField(max_length=50, verbose_name='丁・番地・号')),
                ('building', models.CharField(max_length=50, verbose_name='建物名・部屋番号')),
                ('emargency_contact_number', models.IntegerField(null=True, verbose_name='緊急連絡先(番号)')),
                ('emargency_person', models.CharField(max_length=50, null=True, verbose_name='緊急連絡先（名前）')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'ユーザー',
                'db_table': 'User',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_disease', models.CharField(choices=[('なし', 'なし'), ('あり', 'あり')], max_length=50, verbose_name='心疾患（現在治療要の）')),
                ('cirrhosis', models.CharField(choices=[('なし', 'なし'), ('あり', 'あり')], max_length=50, verbose_name='肝硬変')),
                ('diabetes', models.CharField(choices=[('なし', 'なし'), ('あり', 'あり')], max_length=50, verbose_name='糖尿病')),
                ('chronic_respiratory_disease', models.CharField(choices=[('なし', 'なし'), ('あり', 'あり')], max_length=50, verbose_name='慢性呼吸器疾患（気管支喘息含む）')),
                ('kidoney_disease', models.CharField(choices=[('なし', 'なし'), ('あり', 'あり')], max_length=50, verbose_name='高度慢性腎臓病（GFR30未満が目安）')),
                ('dialysis', models.CharField(choices=[('なし', 'なし'), ('あり', 'あり')], max_length=50, verbose_name='透析')),
                ('malignant_tumor', models.CharField(choices=[('なし', 'なし'), ('あり', 'あり')], max_length=50, verbose_name='治療中の悪性腫瘍')),
                ('immune_lowered_state', models.CharField(choices=[('なし', 'なし'), ('あり', 'あり')], max_length=50, verbose_name='免疫低下状態')),
                ('pregnant', models.CharField(choices=[('いいえ', 'いいえ'), ('はい', 'はい')], max_length=50, verbose_name='37週以降の妊婦')),
                ('vaccination_history', models.CharField(choices=[('0', '打ってない'), ('1', '1回'), ('2', '2回'), ('3', '3回')], max_length=50, verbose_name='ワクチンの接種歴')),
                ('smoking_history', models.CharField(choices=[('なし', 'なし'), ('あり', 'あり')], max_length=50, verbose_name='喫煙歴')),
                ('day_smoking', models.CharField(choices=[('0', 'なし'), ('10', '10本以下'), ('30', '10-30本'), ('50', '50本以上')], max_length=50, verbose_name='喫煙本数/日')),
                ('year_smoking', models.CharField(choices=[('0', 'なし'), ('10', '10年未満'), ('20', '20年以上'), ('30', '30年以上'), ('40', '40年以上'), ('50', '50年以上')], max_length=50, verbose_name='喫煙年数')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_medical', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '既往歴',
                'verbose_name_plural': '既往歴',
                'db_table': 'User_medical_history',
            },
        ),
    ]
