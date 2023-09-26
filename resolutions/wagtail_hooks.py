from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from django.utils.translation import gettext_lazy as _
from .models import Resolutions


class ResolutionsAdmin(ModelAdmin):
    model = Resolutions
    add_to_admin_menu = True
    menu_icon = 'circle-check'
    list_per_page = 50
    chooser_per_page = 10
    list_display = ['name', 'tag']
    #list_filter = ['month', 'year']
    search_fields = ['name']

#modeladmin_register(CustomersGroup)

