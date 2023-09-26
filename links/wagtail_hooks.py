from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Links


class LinksAdmin(ModelAdmin):
    model = Links
    add_to_admin_menu = True
    menu_icon = 'link'
    list_per_page = 50
    chooser_per_page = 10
    list_display = ['name', 'tag']
    #list_filter = ['month', 'year']
    search_fields = ['name']


#modeladmin_register(LinksAdmin)

