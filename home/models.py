# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Qrcode(models.Model):

    #__Qrcode_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Qrcode_FIELDS__END

    class Meta:
        verbose_name        = _("Qrcode")
        verbose_name_plural = _("Qrcode")


class Staticurldata(models.Model):

    #__Staticurldata_FIELDS__
    url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Staticurldata_FIELDS__END

    class Meta:
        verbose_name        = _("Staticurldata")
        verbose_name_plural = _("Staticurldata")



#__MODELS__END
