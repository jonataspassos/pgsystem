import re

from os import path
from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('Mail'), unique=True, validators=[
        validators.RegexValidator(
            re.compile(r'^[\w.@+-]+$'),
            _('Type a valid email. This fields should only contain letters, numbers and the characteres: @/./+/-/_ .'), 'invalid'
        )
    ], help_text=_('Your email address that will be used to access the platform'))
    username = models.CharField(_('Name'), max_length=100)
    # description = models.TextField(_('Description'), blank = True)
    phone = models.CharField(_('Phone'), max_lenght=30, validators=[
        validators.RegexValidator(
            re.compile(r'^((?P<postal>\+?\d{2,3})?[ -]*(?P<ddd>(\(\d{2}\))|\d{2}))?[ -]*(?P<num1>\d{4,5})[ -]*(?P<num2>\d{4})$'),
            _('Phone not recognized'),
            'invalid'
        )
    ])
    image = models.TextField(_('Avatar'), blank= True)
    date_created = models.DateTimeField(_('Create Date'), auto_now_add=True)
    last_update = models.DateTimeField(_('Last Update'), auto_now=True)
    show_email = models.IntegerField(_('Show email?'), null=True, blank=True, choices=(
        (1, _('Allow everyone to see my address')), (2, _('Only classmates can see my address')), (3, _('Nobody can see my address'))), default=1)
    is_staff = models.BooleanField(_('Administrator'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def get_short_name(self):
        return str(self)

    def is_admin(self):
        if self.is_staff:
            return _('Yes')

        return _('Is not an admin')

	#	def get_items(self):
	#		data = Log.objects.filter(user_id = self.id)
	#		return data

