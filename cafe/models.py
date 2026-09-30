from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Posting(models.Model):
    CITY = [
        ['Tai','台北'],['New','新北'],['Ke','基隆'],
        ['Tou','桃園'],['Hsi','新竹'],['Mew','苗栗'],
        ['Taic','台中'],['Chu','彰化'],['Un','雲林'],['Nan','南投'],
        ['Cha','嘉義'],['Tain','台南'],['Kaw','高雄'],['Pei','屏東'],
        ['En','宜蘭'],['Hwa','花蓮'],['Ton','台東'],
        ['Apart','離島'],
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=6, choices=CITY)
    address = models.CharField(max_length=50, null=True)
    price = models.BigIntegerField(default='100')
    wifi = models.BooleanField(default=False)
    limit = models.BooleanField(default=False)
    plugin = models.BooleanField(default=False)
    experience = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='media/img/images/')
    ins = models.URLField(max_length=50, null=True, blank=True)
    pdate = models.DateField(auto_now=True)
    enabled = models.BooleanField(default=False)
    def __str__(self):
        return self.title
