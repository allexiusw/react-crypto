from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Account(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return self.name

    '''
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    '''
