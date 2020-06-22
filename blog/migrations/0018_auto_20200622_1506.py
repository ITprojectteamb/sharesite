# Generated by Django 2.2.13 on 2020-06-22 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_profile_author'),
    ]

    operations = [
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
