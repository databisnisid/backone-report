from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from django.utils.translation import gettext_lazy as _
from resolutions.wagtail_hooks import ResolutionsAdmin
from .models import Reasons


class ReasonsAdmin(ModelAdmin):
    model = Reasons
    add_to_admin_menu = True
    menu_icon = 'error'
    list_per_page = 50
    chooser_per_page = 10
    list_display = ['name', 'tag']
    #list_filter = ['month', 'year']
    search_fields = ['name']


class ReasonsGroup(ModelAdminGroup):
    menu_label = _('Reasons and Resolutions')
    #menu_icon = 'folder-open-inverse'  # change as required
    #menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ReasonsAdmin, ResolutionsAdmin,) 

modeladmin_register(ReasonsGroup)

