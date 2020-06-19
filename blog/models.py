from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import CustomUser

class Profile(models.Model):
    name = models.CharField('社員名（※必須）',max_length=30)
    introduction = models.TextField('ひとこと（※任意）',max_length=200,null=True)
    photo = models.ImageField('プロフィール画像（※任意）',blank=True,null=True)

    def __str__(self):
        return self.name

class Profile_comment(models.Model):
    profile = models.ForeignKey('blog.Profile', on_delete=models.CASCADE, related_name='profile_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField('コメント',null=True)
    created_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Give(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    give_name = models.CharField('タイトル（※必須）',max_length=50)
    give_information = models.TextField('詳細情報（※必須）',max_length=200,null=True)
    give_reason = models.TextField('あげたい理由（※任意）',max_length=200,null=True)
    delivery_infomation = models.CharField('引き渡し方法（※必須）',max_length=30,null=True)
    register_date = models.DateTimeField('登録日時',auto_now_add=True)
    final_update_time = models.DateTimeField('更新日時',auto_now=True)  
    photo = models.ImageField(verbose_name='イメージ写真（※任意）', blank=True, null=True)
    
    def __str__(self):
        return self.give_name

class Give_comment(models.Model):
    give = models.ForeignKey('blog.Give', on_delete=models.CASCADE, related_name='give_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField('コメント',null=True)
    created_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Want(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emergency = (
        ('1', '高'),
        ('2', '中'),
        ('3', '低'),
    )
    emergency_attribute = models.CharField('緊急度（※選択）',max_length=30,choices=emergency)
    want_name = models.CharField('タイトル（※必須）',max_length=50)
    want_information = models.TextField('詳細情報（※必須）',max_length=200,null=True)
    want_reason = models.TextField('ほしい理由（※任意）',max_length=200,null=True)
    register_date = models.DateTimeField('登録日時',auto_now_add=True)
    final_update_time = models.DateTimeField('更新日時',auto_now=True) 
    photo = models.ImageField(verbose_name='イメージ写真（※任意）', blank=True, null=True)

    def __str__(self):
        return self.want_name

class Want_comment(models.Model):
    want = models.ForeignKey('blog.Want', on_delete=models.CASCADE, related_name='want_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField('コメント',null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
