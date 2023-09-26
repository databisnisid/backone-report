from django.db import models
from django.utils.translation import gettext_lazy as _


class Reasons(models.Model):
    name = models.CharField(_('Name'), max_length=300)
    tag = models.CharField(_('Tag'), max_length=30)

    class Meta:
        db_table = 'reasons'
        verbose_name = _('Reason')
        verbose_name_plural = _('Reasons')

    def __str__(self):
        return '{}'.format(self.name)

