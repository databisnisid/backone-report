from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Problems


#class ProblemsSVS(SnippetViewSet):
class ProblemsSVS(ModelAdmin):
    model = Problems
    add_to_admin_menu = True
    menu_icon = 'tag'
    list_per_page = 50
    chooser_per_page = 10
    list_display = ['ticket_number_with_title', 'tags', 'closed_at', 'duration_text']
    list_filter = ['created_at']
    search_fields = ['ticket_number', 'tags']
    readonly_fields = [
            'ticket_number',
            'title',
            'state',
            'priority',
            'group',
            'owner',
            'customer',
            'channel',
            'sender',
            'created_at',
            'closed_at',
            ]


#register_snippet(ProblemsSVS)
modeladmin_register(ProblemsSVS)

