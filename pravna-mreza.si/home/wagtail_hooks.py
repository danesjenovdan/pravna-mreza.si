from django.utils.html import escape
from django.utils.translation import gettext
from draftjs_exporter.dom import DOM
from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler
from wagtail.admin.rich_text.editors.draftail import features as draftail_features
from wagtail.core import hooks
from wagtail.core.rich_text import LinkHandler
from django.utils.text import slugify
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Objava
from novice.models import NovicaTag
from blog.models import Author


class NewTabExternalLinkHandler(LinkHandler):
    identifier = 'external'

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs['href']
        return '<a href="%s" target="_blank">' % escape(href)


def header_with_name(props):
    type_ = props.get('block', {}).get('type', '')
    text = props.get('block', {}).get('text', '')
    tag = 'div'
    if type_ == 'header-two':
        tag = 'h2'
    if type_ == 'header-three':
        tag = 'h3'
    if type_ == 'header-four':
        tag = 'h4'
    return DOM.create_element(tag, {}, DOM.create_element('a', {'id': slugify(text)}), props['children'])


class NovicaTagAdmin(ModelAdmin):
    model = NovicaTag
    menu_label = 'Oznake novic' 
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False 
    exclude_from_explorer = False


class AuthorsAdmin(ModelAdmin):
    model = Author
    menu_label = 'Blog avtorji' 
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False 
    exclude_from_explorer = False


class ObjavaAdmin(ModelAdmin):
    model = Objava
    menu_label = 'Medijska pojavljanja'
    menu_order = 400  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False 
    exclude_from_explorer = False


# Run hook with order=1 so it runs after admin is loaded (default order=0) and overrides rules
@hooks.register('register_rich_text_features', order=1)
def register_extra_rich_text_features(features):
    features.default_features.append('blockquote')

    features.register_link_type(NewTabExternalLinkHandler)

    features.register_converter_rule('contentstate', 'h2', {
        'from_database_format': {
            'h2': BlockElementHandler('header-two'),
        },
        'to_database_format': {
            'block_map': {'header-two': header_with_name}
        }
    })
    features.register_converter_rule('contentstate', 'h3', {
        'from_database_format': {
            'h3': BlockElementHandler('header-three'),
        },
        'to_database_format': {
            'block_map': {'header-three': header_with_name}
        }
    })
    features.register_converter_rule('contentstate', 'h4', {
        'from_database_format': {
            'h4': BlockElementHandler('header-four'),
        },
        'to_database_format': {
            'block_map': {'header-four': header_with_name}
        }
    })


modeladmin_register(NovicaTagAdmin)
modeladmin_register(AuthorsAdmin)
modeladmin_register(ObjavaAdmin)
