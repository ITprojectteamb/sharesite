from django import forms

from .models import Post,Give,Want

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class GiveForm(forms.ModelForm):

    class Meta:
        model = Give
        fields = ('title', 'text',)

class WantForm(forms.ModelForm):

    class Meta:
        model = Want
        fields = ('title', 'text',)