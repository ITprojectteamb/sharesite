from django.conf import settings
from django.db import models
from django.utils import timezone


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

class Want(models.Model):
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


##################################################################
#ここから先追加箇所＃
##################################################################

##################################################################
#ここから高橋追加＃
##################################################################

class Item(models.Model):
    item_id = models.CharField(max_length=7)
    mail_address = models.EmailField('メールアドレス')
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
    mail_address = models.EmailField('メールアドレス')
    passward = models.CharField('パスワード',max_length=20)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField('社員名',max_length=30)
    mail_address = models.EmailField('メールアドレス')
    introduction = models.CharField('自己紹介',max_length=200)
    item_image = models.ImageField('プロフィール画像',null=True)

    def __str__(self):
        return self.name


class Give(models.Model):
    give_id = models.CharField(max_length=7)
    give_name = models.CharField('GIVEアイテム名称',max_length=30)
    item_id = models.CharField(max_length=7)
    delivery_infomation = models.TextField('引き渡し情報',max_length=200,null=True)
    give_reason = models.TextField('あげたい理由',max_length=200,null=True)
    register_date = models.DateTimeField('登録日時',default=timezone.now)
    open_date = models.DateTimeField('公開日時',blank=True, null=True)
    final_update_time = models.DateTimeField('更新日時',default=timezone.now,) 
    delite_flug =  models.BooleanField('論理削除フラグ', default=False)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    
    def __str__(self):
        return self.give_name

class Give_comment(models.Model):
    give_comment_id = models.CharField(max_length=7)
    give_id = models.CharField(max_length=7)
    give_comment = models.CharField('GIVEコメント',max_length=200)
    employee_name = models.CharField('社員名',max_length=30)
    register_date = models.DateTimeField('登録日時',default=timezone.now)
    delite_flug =  models.BooleanField('論理削除フラグ', default=False)
    
    def __str__(self):
        return self.give_comment_id

class Want_info(models.Model):
    want_id = models.CharField(max_length=7)
    mail_address = models.EmailField('メールアドレス')
    want_name = models.CharField('WANTタイトル',max_length=30)
    introduction = models.CharField('WANT詳細',max_length=200)
    item_image = models.ImageField(null=True)
    delivery_infomation = models.TextField('引き渡し情報',max_length=200,null=True)
    give_reason = models.TextField('あげたい理由',max_length=200,null=True)
    register_date = models.DateTimeField('登録日時',default=timezone.now)
    open_date = models.DateTimeField('公開日時',blank=True, null=True)
    final_update_time = models.DateTimeField('更新日時',default=timezone.now,) 
    delite_flug =  models.BooleanField('論理削除フラグ', default=False)    
    photo = models.ImageField(verbose_name='写真1', blank=True, null=True)

    def __str__(self):
        return self.want_name

class Want_comment(models.Model):
    want_comment_id = models.CharField(max_length=7)
    want_id = models.CharField(max_length=7)
    want_comment = models.CharField('WANTコメント',max_length=200)
    employee_name = models.CharField('社員名',max_length=30)
    register_date = models.DateTimeField('登録日時',default=timezone.now)
    delite_flug =  models.BooleanField('論理削除フラグ', default=False)
    
    def __str__(self):
        return self.give_comment_id