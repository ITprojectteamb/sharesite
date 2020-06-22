# Generated by Django 2.2.13 on 2020-06-22 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_auto_20200619_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='final_update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時'),
        ),
        migrations.AddField(
            model_name='profile',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時'),
        ),
        migrations.AlterField(
            model_name='give',
            name='final_update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='give',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時'),
        ),
        migrations.AlterField(
            model_name='want',
            name='final_update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='want',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時'),
        ),
    ]
