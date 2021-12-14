from django.utils.translation import gettext_lazy as _
from django.db import models
from novice.models import NovicaPage
from blog.models import BlogPage
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
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
    title = models.TextField(null=True, blank=True, verbose_name='Naslov (neobvezno)')
    text = RichTextField(verbose_name='Opis')
    page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Povezava do strani (neobvezno)')
    page_text = models.TextField(null=True, blank=True, verbose_name='Besedilo na gumbu s povezavo (neobvezno)')

    panels = [
        FieldPanel('title'),
        FieldPanel('text', classname="full"),
        FieldPanel('page_text'),
        PageChooserPanel('page'),
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
    intro_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    news_section_title = models.TextField(verbose_name='Naslov sekcije z novicami')
    news_section_archive_link_title = models.TextField(verbose_name='Ime povezave do seznama novic')
    news_section_archive_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Povezava do seznama novic')
    social_media_title_part_one = models.TextField(verbose_name='Škatla socialna omrežja - naslov 1. del')
    social_media_title_part_two = models.TextField(verbose_name='Škatla socialna omrežja - naslov 2. del')
    facebook_link = models.URLField(verbose_name='Facebook URL')
    twitter_link = models.URLField(verbose_name='Twitter URL')
    newsletter_title_part_one = models.TextField(verbose_name='Škatla novičnik - naslov 1. del')
    newsletter_title_part_two = models.TextField(verbose_name='Škatla novičnik - naslov 2. del')
    newsletter_terms = models.TextField(verbose_name='Škatla novičnik - pogoji')
    newsletter_button = models.TextField(verbose_name='Škatla novičnik - gumb')
    blog_section_title = models.TextField(verbose_name='Naslov blog sekcije')
    blog_section_archive_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name='Povezava do seznama blog zapisov')
    blog_section_archive_link_title = models.TextField(verbose_name='Ime povezave do seznama blog zapisov')
    support_title_part_one = models.TextField(verbose_name='Škatla podpri - naslov 1. del')
    support_title_part_two = models.TextField(verbose_name='Škatla podpri - naslov 2. del')
    support_text = models.TextField(verbose_name='Škatla podpri - opis')
    support_button = models.TextField(verbose_name='Škatla podpri - gumb')
    monitor_title_part_one = models.TextField(verbose_name='Škatla monitoring - naslov 1. del')
    monitor_title_part_two = models.TextField(verbose_name='Škatla monitoring - naslov 2. del')
    monitor_text = models.TextField(verbose_name='Škatla monitoring - opis')
    monitor_button = models.TextField(verbose_name='Škatla monitoring - gumb')

    content_panels = Page.content_panels + [
        FieldPanel('intro_text', classname="full"),
        ImageChooserPanel('intro_image'),
        FieldPanel('news_section_title'),
        FieldPanel('news_section_archive_link_title'),
        FieldPanel('news_section_archive_link'),
        FieldPanel('social_media_title_part_one'),
        FieldPanel('social_media_title_part_two'),
        FieldPanel('facebook_link'),
        FieldPanel('twitter_link'),
        FieldPanel('newsletter_title_part_one'),
        FieldPanel('newsletter_title_part_two'),
        FieldPanel('newsletter_terms'),
        FieldPanel('newsletter_button'),
        FieldPanel('blog_section_title'),
        FieldPanel('blog_section_archive_link'),
        FieldPanel('blog_section_archive_link_title'),
        FieldPanel('support_title_part_one'),
        FieldPanel('support_title_part_two'),
        FieldPanel('support_text'),
        FieldPanel('support_button'),
        FieldPanel('monitor_title_part_one'),
        FieldPanel('monitor_title_part_two'),
        FieldPanel('monitor_text'),
        FieldPanel('monitor_button'),
    ]

    parent_page_types = []

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        novice = NovicaPage.objects.all().live().order_by('-first_published_at')[:3]
        blogposts = BlogPage.objects.all().live().order_by('-first_published_at')[:1]
        pojavljanja = Objava.objects.all().order_by('-date')[:3]
        context['novice'] = novice
        context['blogposts'] = blogposts
        # context['pojavljanja'] = pojavljanja
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