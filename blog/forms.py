from django import forms
from django.core.mail import EmailMessage

from .models import Give,Want,Profile,Give_comment,Want_comment,Profile_comment

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('name','introduction','photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GiveCreateForm(forms.ModelForm):
    class Meta:
        model = Give
        fields = ('author', 'give_name','give_information', 'give_reason','delivery_infomation', 'photo')

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
        fields = ('author','want_name', 'want_information', 'want_reason','emergency_attribute', 'photo')

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