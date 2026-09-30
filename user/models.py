from django.db import models
from django.contrib.auth.models import User
from cafe.models import Posting
# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
