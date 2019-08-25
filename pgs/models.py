from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class PequenoGrupo(models.Model):
    name = models.CharField(_('PG Name'),default='PG MyStyle',max_length=30)
    leader = models.ManyToManyField(User,related_name='leader')
    participant = models.ManyToManyField(User,related_name='participant')
    def __str__(self):
        return self.name

class Responsible(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    children=models.ManyToManyField(User,related_name='Children')
    def __str__(self):
        return self.user.nickname
