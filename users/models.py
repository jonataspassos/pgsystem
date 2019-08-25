import re

from os import path
from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils import timezone

# Create your models here.

def validate_img_extension(value):
    valid_formats = ['image/jpeg','image/x-citrix-jpeg','image/png','image/x-citrix-png','image/x-png']

    if hasattr(value.file, 'content_type'):
        if not value.file.content_type in valid_formats:
            raise ValidationError(_('File not supported.'))

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(default="jonjomeutunos@gmail.com")
    nickname = models.CharField(_('NickName'),unique=True, max_length=30)
    username = models.CharField(_('Name'), max_length=100)
    # description = models.TextField(_('Description'), blank = True)
    phone = models.CharField(_('Phone'), max_length=30, validators=[
        validators.RegexValidator(
            re.compile(r'^((?P<postal>\+?\d{2,3})?[ -]*(?P<ddd>(\(\d{2}\))|\d{2}))?[ -]*(?P<num1>\d{4,5})[ -]*(?P<num2>\d{4})$'),
            _('Phone not recognized'),
            'invalid'
        )
    ])
    birth=models.DateField(_('Birth Date'), default=timezone.now)
    image = models.ImageField(verbose_name = _('Photo'), null=True, blank = True, upload_to = 'users/static/users/img/photos/', validators = [validate_img_extension])
    date_created = models.DateTimeField(_('Create Date'), auto_now_add=True)
    last_update = models.DateTimeField(_('Last Update'), auto_now=True)
    is_staff = models.BooleanField(_('Administrator'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)

    # EMAIL_FIELD = 'nickname'
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['username','email']

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def get_short_name(self):
        return str(self)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            if path.exists(self.image.path):
                return self.image.url
		
        return static('img/no_image.jpg')

    def is_admin(self):
        if self.is_staff:
            return _('Yes')

        return _('Is not an admin')

	#	def get_items(self):
	#		data = Log.objects.filter(user_id = self.id)
	#		return data