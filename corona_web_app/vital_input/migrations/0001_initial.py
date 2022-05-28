# Generated by Django 4.0.4 on 2022-05-26 03:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vital_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('BodyTemperature', models.FloatField(validators=[django.core.validators.MinValueValidator(30.0), django.core.validators.MaxValueValidator(50.0)])),
                ('SpO2', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('Sbp', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('Dbp', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('Pulse', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('Dyspnea', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='息苦しさ')),
                ('ChestPain', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='胸の痛み')),
                ('Fatigue', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='倦怠感（だるさ）')),
                ('Chills', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='悪寒')),
                ('Cough', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='咳')),
                ('RunnyNose', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='鼻水')),
                ('Nausea', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='嘔気')),
                ('Vomiting', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='嘔吐')),
                ('Diarrhea', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='下痢')),
                ('Headache', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='頭痛')),
                ('Stomachace', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='腹痛')),
                ('JointPain', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='関節痛')),
                ('Dysosmia', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='嗅覚異常')),
                ('Dysgeusia', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='味覚異常')),
                ('Convulsion', models.TextField(blank=True, choices=[('無', 'なし'), ('少し', '少しある'), ('有', 'ある'), ('不明', '分からない')], verbose_name='けいれん')),
                ('LossOfAppetite', models.TextField(blank=True, choices=[('有', 'ある'), ('少し', '少しある'), ('無', 'なし'), ('不明', '分からない')], verbose_name='食欲')),
                ('MealAmount', models.TextField(blank=True, choices=[('0', 'いつも通り'), ('1', 'いつもより少ないが、食べれている'), ('2', '全く食べれていない'), ('3', '不明')], verbose_name='食事量')),
                ('AmountOfWater', models.TextField(blank=True, choices=[('0', '1L以上'), ('1', '500ml~1L'), ('2', '500ml未満'), ('3', '不明')], verbose_name='水分量')),
                ('NumberOfAntipyretics', models.TextField(blank=True, choices=[('0', '6回分以上'), ('1', '3~5回分'), ('2', '持っていない')], verbose_name='解熱剤の残数')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_vital', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
