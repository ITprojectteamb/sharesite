from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Item(models.Model):
    item_id = models.CharField(max_length=7)
    mail_address = models.EmailField('メールアドレス',null=True)
    item_name = models.CharField('アイテム名称',max_length=20)
    item_detail = models.TextField('アイテム詳細',max_length=200,blank=True,null=True)
    attribute_list= (
        ('object', 'オブジェクト'),
        ('skill', 'スキル'),
    )
    item_attribute = models.CharField('属性',max_length=30,choices=attribute_list)
    item_image = models.ImageField()
    
    def __str__(self):
        return self.item_name

class Employee(models.Model):
    name = models.CharField('社員名',max_length=30)
    mail_address = models.EmailField('メールアドレス',null=True)
    passward = models.CharField('パスワード',max_length=20)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField('社員名',max_length=30)
    mail_address = models.EmailField('メールアドレス',null=True)
    introduction = models.CharField('自己紹介',max_length=200,null=True)
    photo = models.ImageField('プロフィール画像',blank=True,null=True)

    def __str__(self):
        return self.name

class Profile_comment(models.Model):
    profile = models.ForeignKey('blog.Profile', on_delete=models.CASCADE, related_name='profile_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField('PROFILEコメント',null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    delite_flug =  models.BooleanField('論理削除フラグ', default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Give(models.Model):
    give_name = models.CharField('GIVEアイテム名称',max_length=30)
    give_information = models.TextField('商品詳細情報',max_length=200,null=True)
    give_reason = models.TextField('あげたい理由',max_length=200,null=True)
    delivery_infomation = models.CharField('引き渡し方法',max_length=30,null=True)
    register_date = models.DateTimeField('登録日時',default=timezone.now)
    final_update_time = models.DateTimeField('更新日時',default=timezone.now,) 
    photo = models.ImageField(verbose_name='イメージ写真', blank=True, null=True)
    
    def __str__(self):
        return self.give_name

class Give_comment(models.Model):
    give = models.ForeignKey('blog.Give', on_delete=models.CASCADE, related_name='give_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField('GIVEコメント',null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    delite_flug =  models.BooleanField('論理削除フラグ', default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Want(models.Model):
    want_name = models.CharField('WANTアイテム名称',max_length=30)
    want_information = models.TextField('商品詳細情報',max_length=200,null=True)
    want_reason = models.TextField('ほしい理由',max_length=200,null=True)
    delivery_infomation = models.CharField('引き渡し方法',max_length=30,null=True)
    register_date = models.DateTimeField('登録日時',default=timezone.now)
    final_update_time = models.DateTimeField('更新日時',default=timezone.now,) 
    photo = models.ImageField(verbose_name='イメージ写真', blank=True, null=True)

    def __str__(self):
        return self.want_name

class Want_comment(models.Model):
    want = models.ForeignKey('blog.Want', on_delete=models.CASCADE, related_name='want_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField('WANTコメント',null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    delite_flug =  models.BooleanField('論理削除フラグ', default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
