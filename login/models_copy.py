from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uName = models.CharField(max_length=50)
    uPass = models.CharField(max_length=50)
    uSix = models.NullBooleanField(default=None)


