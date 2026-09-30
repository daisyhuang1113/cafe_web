from django import forms
from . import models


# class PostingForm(forms.ModelForm):
#     class Meta:
#         model = models.Posting
#         fields = [
#         'title', 'city', 'address', 'price', 'wifi', 'limit', 'plugin',
#         'experience', 'picture', 'ins', 'enabled']
#     def __init__(self, *args, **kwargs):
#         super(PostingForm, self).__init__(*args, **kwargs)
#         self.fields['title'].label = '店名'
#         self.fields['city'].label = '座落城市'
#         self.fields['address'].label = '地址'
#         self.fields['price'].label = '平均價格'
#         self.fields['wifi'].label = '是否有網路？'
#         self.fields['limit'].label = '是否限時？'
#         self.fields['plugin'].label = '是否有插座？'
#         self.fields['experience'].label = '說說你的經驗'
#         self.fields['picture'].label = '照片'
#         self.fields['ins'].label = '你的個人網站'
#         self.fields['enabled'].label = '是否公開'

class SearchForm(forms.Form):
    CITY = [
        ['Tai','台北'],['New','新北'],['Ke','基隆'],
        ['Tou','桃園'],['Hsi','新竹'],['Mew','苗栗'],
        ['Taic','台中'],['Chu','彰化'],['Un','雲林'],['Nan','南投'],
        ['Cha','嘉義'],['Tain','台南'],['Kaw','高雄'],['Pei','屏東'],
        ['En','宜蘭'],['Hwa','花蓮'],['Ton','台東'],
        ['Apart','離島'],
    ]
    w_wifi = forms.BooleanField(label = "有網路", required=False)
    w_limit = forms.BooleanField(label = "限時", required=False)
    w_plugin = forms.BooleanField(label = "有插座", required=False)
    city = forms.ChoiceField(label = "城市", choices = CITY)
