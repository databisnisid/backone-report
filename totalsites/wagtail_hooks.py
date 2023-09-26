from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from django.utils.translation import gettext_lazy as _
from .models import TotalSites
from companies.wagtail_hooks import CompaniesAdmin


class TotalSitesAdmin(ModelAdmin):
    model = TotalSites
    add_to_admin_menu = True
    menu_icon = 'site'
    list_per_page = 50
    chooser_per_page = 10
    list_display = ['company', 'month', 'year', 'total_sites']
    list_filter = ['month', 'year']
    search_fields = ['company__name']

class TotalSitesGroup(ModelAdminGroup):
    menu_label = _('Companies and Total Sites')
    items = (CompaniesAdmin, TotalSitesAdmin,) 

modeladmin_register(TotalSitesGroup)

