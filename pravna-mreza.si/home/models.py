from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from novice.models import NovicaPage


class HomePage(Page):
    intro_text = RichTextField(blank=True, null=True)
    description_text = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro_text', classname="full"),
        FieldPanel('description_text', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        novice = NovicaPage.objects.all().live().order_by('-first_published_at')
        context['novice'] = novice
        return context
