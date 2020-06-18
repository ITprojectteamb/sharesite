from django import forms
from django.core.mail import EmailMessage

from .models import Post,Give,Want,Profile,Item,Employee,Give_comment,Want_comment,Profile_comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('name','mail_address','introduction','photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GiveCreateForm(forms.ModelForm):
    class Meta:
        model = Give
        fields = ('give_name','give_information', 'give_reason','delivery_infomation', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GiveCommentForm(forms.ModelForm):
    class Meta:
        model = Give_comment
        fields = ('author', 'text',)

class WantCreateForm(forms.ModelForm):
    class Meta:
        model = Want
        fields = ('want_name', 'want_information', 'want_reason','delivery_infomation', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class WantCommentForm(forms.ModelForm):

    class Meta:
        model = Want_comment
        fields = ('author', 'text',)

class ProfileCommentForm(forms.ModelForm):

    class Meta:
        model = Profile_comment
        fields = ('author', 'text',)