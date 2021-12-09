from django.utils.translation import gettext_lazy as _
from django.db import models
from novice.models import NovicaPage
from blog.models import BlogPage
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.snippets.models import register_snippet


class ExternalLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(label=_('Ime'))
    url = blocks.URLBlock(label=_('Povezava'))
    has_border = blocks.BooleanBlock(label='Gumb ima obrobo?', required=False)

    class Meta:
        label = _('Zunanja povezava')
        icon = 'link'


class PageLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=False, label=_('Ime'), help_text=_('Če je prazno se uporabi naslov strani.'))
    page = blocks.PageChooserBlock(label=_('Stran'))
    has_border = blocks.BooleanBlock(label='Gumb ima obrobo?', required=False)

    class Meta:
        label = _('Povezava do strani')
        icon = 'link'


@register_snippet
class Infopush(models.Model):
    title = models.TextField(null=True, blank=True)
    text = RichTextField()

    panels = [
        FieldPanel('title'),
        FieldPanel('text', classname="full")
    ]

    def __str__(self):
        return self.title


@register_setting
class OgSettings(BaseSetting):
    og_title = models.CharField(max_length=255)
    og_description = models.CharField(max_length=255)
    og_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('og_title'),
        FieldPanel('og_description'),
        ImageChooserPanel('og_image'),
    ]


@register_setting()
class NavigationSettings(BaseSetting):
    navigation_links = StreamField(
        [
            ('page_link', PageLinkBlock()),
            ('external_link', ExternalLinkBlock()),
        ],
        verbose_name=_("Povezave v glavi"),
    )
    # footer_links = StreamField(
    #     [
    #         ("page_link", blocks.PageLinkBlock()),
    #         ("external_link", blocks.ExternalLinkBlock()),
    #     ],
    #     verbose_name=_("Povezave v nogi"),
    #     )

    panels = [
        StreamFieldPanel("navigation_links"),
        # StreamFieldPanel("footer_links"),
    ]

    class Meta:
        verbose_name = 'Navigacija'



class Objava(models.Model):
    title = models.TextField()
    url = models.URLField()
    source = models.TextField()
    date = models.DateField()

    panels = [
        FieldPanel('title'),
        FieldPanel('url', classname="full"),
        FieldPanel('source'),
        FieldPanel('date'),
    ]

    def __str__(self):
        return self.title


class HomePage(Page):
    intro_text = RichTextField(blank=True, null=True)
    description_text = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro_text', classname="full"),
        FieldPanel('description_text', classname="full")
    ]

    parent_page_types = []

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        novice = NovicaPage.objects.all().live().order_by('-first_published_at')[:3]
        blogposts = BlogPage.objects.all().live().order_by('-first_published_at')[:3]
        pojavljanja = Objava.objects.all().order_by('-date')[:3]
        context['novice'] = novice
        context['blogposts'] = blogposts
        context['pojavljanja'] = pojavljanja
        return context


class GenericPage(Page):
    body = StreamField([
        ('heading', blocks.StructBlock([
            ('part_one', blocks.CharBlock(required=False)),
            ('part_two', blocks.CharBlock(required=False)),
            ('intro_text', blocks.RichTextBlock(required=False)),
        ], icon='title')),
        ('paragraph', blocks.RichTextBlock()),
        ('donation_section', blocks.StructBlock([
            ('left_button_heading_part_one', blocks.CharBlock(required=False, label=_('Levi gumb - Prvi del naslova'))),
            ('left_button_heading_part_two', blocks.CharBlock(required=False, label=_('Levi gumb - Drugi del naslova'))),
            ('left_button_description', blocks.CharBlock(required=False, label=_('Levi gumb - Podnaslov'))),
            ('left_button_donation_page', blocks.PageChooserBlock(
                label=_('Levi gumb - Povezava do strani'),
            )),
            ('right_button_heading_part_one', blocks.CharBlock(required=False, label=_('Desni gumb - Prvi del naslova'))),
            ('right_button_heading_part_two', blocks.CharBlock(required=False, label=_('Desni gumb - Drugi del naslova'))),
            ('right_button_description', blocks.CharBlock(required=False, label=_('Desni gumb - Podnaslov'))),
            ('right_button_donation_page', blocks.PageChooserBlock(
                label=_('Desni gumb - Povezava do strani'),
            )),
        ]))
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class DonationEmbedPage(Page):
    embed_url = models.URLField()

    content_panels = Page.content_panels + [
        FieldPanel('embed_url', classname="full"),
    ]


class NewsletterPage(Page):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Opis"),
    )
    # body = StreamField(
    #     [("rich_text", RichTextBlock())],
    #     null=True,
    #     blank=True,
    #     verbose_name=_("Vsebina"),
    # )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        # StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Urejanje naročnine"
        verbose_name_plural = "Urejanja naročnin"