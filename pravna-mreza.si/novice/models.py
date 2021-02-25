from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


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

class NovicaArchivePage(Page):
    body = StreamField([
        ('heading', blocks.StructBlock([
            ('part_one', blocks.CharBlock(required=False)),
            ('part_two', blocks.CharBlock(required=False)),
        ], icon='title'))
        ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        # Get all novice
        vse_novice = NovicaPage.objects.all().live().order_by('-first_published_at')
        # Paginate all novice by 2 per page
        paginator = Paginator(vse_novice, 10)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            novice = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            novice = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            novice = paginator.page(paginator.num_pages)
        context['novice'] = novice
        return context
