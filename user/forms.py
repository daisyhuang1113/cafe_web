from django import forms
from . import models
from cafe import models

class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=20, \
    widget=forms.TextInput(attrs={'placeholder': 'accounts'}))
    password = forms.CharField(label="", max_length=20, \
    widget = forms.PasswordInput(attrs={'placeholder': 'password'}))

class PostingForm(forms.ModelForm):
    class Meta:
        model = models.Posting
        fields = [
        'title', 'city', 'address', 'price', 'wifi', 'limit', 'plugin',
        'experience', 'picture', 'ins', 'enabled']
    def __init__(self, *args, **kwargs):
        super(PostingForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '店名'
        self.fields['city'].label = '座落城市'
        self.fields['address'].label = '地址'
        self.fields['price'].label = '平均價格'
        self.fields['wifi'].label = '是否有網路？'
        self.fields['limit'].label = '是否限時？'
        self.fields['plugin'].label = '是否有插座？'
        self.fields['experience'].label = '說說你的經驗'
        self.fields['picture'].label = '照片'
        self.fields['ins'].label = '你的個人網站'
        self.fields['enabled'].label = '是否公開'
