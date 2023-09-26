from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from django.utils.translation import gettext_lazy as _
from .models import Customers
from links.wagtail_hooks import LinksAdmin


class CustomersAdmin(ModelAdmin):
    model = Customers
    add_to_admin_menu = True
    menu_icon = 'globe'
    list_per_page = 50
    chooser_per_page = 10
    list_display = ['name', 'tag']
    #list_filter = ['month', 'year']
    search_fields = ['name']

class CustomersGroup(ModelAdminGroup):
    menu_label = _('Customers and Links')
    #menu_icon = 'folder-open-inverse'  # change as required
    #menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (CustomersAdmin, LinksAdmin,) 

modeladmin_register(CustomersGroup)

