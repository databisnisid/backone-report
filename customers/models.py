from django.db import models
from django.utils.translation import gettext_lazy as _


class Customers(models.Model):
    name = models.CharField(_('Name'), max_length=300)
    tag = models.CharField(_('Tag'), max_length=30)

    class Meta:
        db_table = 'customers'
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return '{}'.format(self.name)

