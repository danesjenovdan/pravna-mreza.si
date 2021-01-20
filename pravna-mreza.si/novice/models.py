from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page


class NovicaPage(Page):
    date = models.DateField()
    preview_text = RichTextField(blank=False, null=False, default='')
    body = StreamField([
        ('heading', blocks.StructBlock([
            ('part_one', blocks.CharBlock(required=False)),
            ('part_two', blocks.CharBlock(required=False)),
            ('intro_text', blocks.RichTextBlock(required=False)),
        ], icon='title')),
        ('paragraph', blocks.RichTextBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('preview_text', classname="full"),
        StreamFieldPanel('body'),
    ]
