# Generated by Django 2.2.13 on 2020-06-16 02:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='社員名')),
                ('mail_address', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('passward', models.CharField(max_length=20, verbose_name='パスワード')),
            ],
        ),
        migrations.CreateModel(
            name='Give_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('give_comment_id', models.CharField(max_length=7)),
                ('give_id', models.CharField(max_length=7)),
                ('give_comment', models.CharField(max_length=200, verbose_name='GIVEコメント')),
                ('employee_name', models.CharField(max_length=30, verbose_name='社員名')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('delite_flug', models.BooleanField(default=False, verbose_name='論理削除フラグ')),
            ],
        ),
        migrations.CreateModel(
            name='Give_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('give_id', models.CharField(max_length=7)),
                ('give_name', models.CharField(max_length=30, verbose_name='GIVEアイテム名称')),
                ('item_id', models.CharField(max_length=7)),
                ('delivery_infomation', models.TextField(max_length=200, null=True, verbose_name='引き渡し情報')),
                ('give_reason', models.TextField(max_length=200, null=True, verbose_name='あげたい理由')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('open_date', models.DateTimeField(blank=True, null=True, verbose_name='公開日時')),
                ('final_update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日時')),
                ('delite_flug', models.BooleanField(default=False, verbose_name='論理削除フラグ')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=7)),
                ('mail_address', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('item_name', models.CharField(max_length=20, verbose_name='アイテム名称')),
                ('item_detail', models.TextField(blank=True, max_length=200, null=True, verbose_name='アイテム詳細')),
                ('item_attribute', models.CharField(choices=[('object', 'オブジェクト'), ('skill', 'スキル')], max_length=30, verbose_name='属性')),
                ('item_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Want_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('want_comment_id', models.CharField(max_length=7)),
                ('want_id', models.CharField(max_length=7)),
                ('want_comment', models.CharField(max_length=200, verbose_name='WANTコメント')),
                ('employee_name', models.CharField(max_length=30, verbose_name='社員名')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('delite_flug', models.BooleanField(default=False, verbose_name='論理削除フラグ')),
            ],
        ),
        migrations.CreateModel(
            name='Want_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('want_id', models.CharField(max_length=7)),
                ('mail_address', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('want_name', models.CharField(max_length=30, verbose_name='WANTタイトル')),
                ('introduction', models.CharField(max_length=200, verbose_name='WANT詳細')),
                ('item_image', models.ImageField(null=True, upload_to='')),
                ('delivery_infomation', models.TextField(max_length=200, null=True, verbose_name='引き渡し情報')),
                ('give_reason', models.TextField(max_length=200, null=True, verbose_name='あげたい理由')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('open_date', models.DateTimeField(blank=True, null=True, verbose_name='公開日時')),
                ('final_update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日時')),
                ('delite_flug', models.BooleanField(default=False, verbose_name='論理削除フラグ')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='author',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='text',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
        migrations.AddField(
            model_name='profile',
            name='introduction',
            field=models.CharField(default=1, max_length=200, verbose_name='自己紹介'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='item_image',
            field=models.ImageField(null=True, upload_to='', verbose_name='プロフィール画像'),
        ),
        migrations.AddField(
            model_name='profile',
            name='mail_address',
            field=models.EmailField(default=1, max_length=254, verbose_name='メールアドレス'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=1, max_length=30, verbose_name='社員名'),
            preserve_default=False,
        ),
    ]
