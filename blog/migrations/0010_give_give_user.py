# Generated by Django 2.2.13 on 2020-06-17 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20200617_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='give',
            name='give_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
            preserve_default=False,
        ),
    ]