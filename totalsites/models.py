from django.db import models
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _
from companies.models import Companies

MONTHS = (
        (1, _('January')),
        (2, _('February')),
        (3, _('March')),
        (4, _('April')),
        (5, _('May')),
        (6, _('June')),
        (7, _('July')),
        (8, _('August')),
        (9, _('September')),
        (10, _('October')),
        (11, _('November')),
        (12, _('December')),
        )

YEARS = (
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
        (2028, '2028'),
        (2029, '2029'),
        (2030, '2030'),
        )

class TotalSites(models.Model):
    company = models.ForeignKey(
            Companies,
            on_delete=models.CASCADE,
            verbose_name=_('Company')
            )
    month = models.IntegerField(
            choices=MONTHS,
            default=1,
            )
    year = models.IntegerField(
            choices=YEARS,
            default=2023,
            )
    total_sites = models.IntegerField()

    class Meta:
        db_table = 'totalsites'
        verbose_name = _('Total Site')
        verbose_name_plural = _('Total Sites')

    def __str__(self):
        return '{}'.format(self.company)

    def clean(self):
        try:
            TotalSites.objects.get(
                    company=self.company,
                    month=self.month,
                    year=self.year
                    )
            raise ValidationError(_('Record is already exists!'))

        except models.ObjectDoesNotExist:
            pass
