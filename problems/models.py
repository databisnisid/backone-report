from enum import unique
from django.contrib.admin.options import format_html
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from config.utils import readable_timedelta


class Problems(models.Model):
    ticket_number = models.CharField(_('Ticket Number'), max_length=30, unique=True)
    title = models.CharField(_('Title'), max_length=300)
    state = models.CharField(_('State'), max_length=30)
    priority = models.CharField(_('Priority'), max_length=30)
    group = models.CharField(_('Group'), max_length=30)
    owner = models.CharField(_('Owner'), max_length=30)
    customer = models.CharField(_('Customer'), max_length=30)
    channel = models.CharField(_('Create Channel'), max_length=30)
    sender = models.CharField(_('Sender'), max_length=30)
    tags = models.CharField(_('Tags'), max_length=300)
    created_at = models.DateTimeField(_('Created At'))
    closed_at = models.DateTimeField(_('Closed At'))
    duration = models.IntegerField()

    class Meta:
        db_table = 'problems'
        verbose_name = _('Problem')
        verbose_name_plural = _('Problems')

    def __str__(self):
        return '{}'.format(self.ticket_number)

    def save(self, *args, **kwargs):
        timedelta = self.closed_at - self.created_at
        self.duration = timedelta.total_seconds()

        return super(Problems, self).save(*args, **kwargs)

    def ticket_number_with_title(self):
        return format_html('{}<br />{}', self.ticket_number, self.title)
    ticket_number_with_title.short_description = _('Ticket Number')

    def duration_text(self):
        #return readable_timedelta(self.created_at, self.closed_at)
        return readable_timedelta(self.duration)
    duration_text.short_description = _('Duration')

