from django.forms import ModelForm
from .models import SnsappPost

class SnsappPostForm(ModelForm):
    class Meta:
        model = SnsappPost
        fields = ['comment', 'image1', 'image2','image3','image4']


from django.forms import ModelForm
from django import forms
from .models import SnsappPost

class SnsappPostForm(ModelForm):
    class Meta:
        model = SnsappPost
        fields = ['comment', 'image1', 'image2','image3','image4']

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = \
            'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = \
            'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'