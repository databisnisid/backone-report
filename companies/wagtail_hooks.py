from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Companies


class CompaniesAdmin(ModelAdmin):
    model = Companies
    add_to_admin_menu = True
    menu_icon = 'home'
    list_per_page = 50
    chooser_per_page = 10
    list_display = ['name', 'tag']
    #list_filter = ['month', 'year']
    search_fields = ['name']


#modeladmin_register(CompaniesAdmin)

